"""
HDF5 LOAD DATA QDialog (crikit.vis.subguis.h5loadgui)
=======================================================

    H5LoadGUI : A graphical user interface (GUI) to select HDF5 dataset(s)

    Method : H5LoadGUI.getFileDataSets()

    Return (tuple) : (path [str], filename [str], dataset(s) [list], selection_made [bool])

    Notes
    -----
    Methods that interact with Qt follow the Qt naming convention:
    firstSecondThird
"""

# Append sys path
import sys as _sys
import os as _os

from PyQt5.QtCore import Qt

try:
    # Generic imports for QT-based programs
    from PyQt5.QtWidgets import (QApplication as _QApplication, \
    QDialog as _QDialog, QFileDialog as _QFileDialog, \
    QTableWidgetItem as _QTableWidgetItem)
except:
    HAS_PYQT5 = False
else:
    HAS_PYQT5 = True
from lazy5.ui.qt_HdfLoad import Ui_Dialog

from lazy5.inspect import get_hierarchy, get_attrs_dset, get_attrs_group
from lazy5.nonh5utils import filterlist
from lazy5 import alter

class HdfLoad(_QDialog): ### EDIT ###
    """ GUI Loader Class for H5 Files """

    # Default configuration
    config = {'only_show_grp_w_dset': False,  # Only show groups with datasets
              'excl_filtering' : True  # Filtering is exclusive (filters are AND'd)
             }

    def __init__(self, title=None, parent=None):

        # Generic load/init designer-based GUI
        super(HdfLoad, self).__init__(parent)
        self.ui = Ui_Dialog()  # pylint: disable=C0103
        self.ui.setupUi(self)
        
        self.ui.tableAttributes.itemChanged.connect(self.update_attrs_to_file)

        self.path = None
        self.filename = None
        self.all_selected = None
        self.group_dset_dict = None

        if title:
            self.setWindowTitle('{}: Select a dataset...'.format(title))
        else:
            self.setWindowTitle('Select a dataset...')

        self.ui.pushButtonOk.clicked.connect(self.accept)
        self.ui.pushButtonCancel.clicked.connect(self.reject)
        self.ui.comboBoxGroupSelect.currentTextChanged.connect(self.dataGroupChange)
        self.ui.listDataSet.itemClicked.connect(self.datasetSelected)
        self.ui.pushButtonFilter.clicked.connect(self.filterDatasets)
        self.ui.pushButtonResetFilter.clicked.connect(self.dataGroupChange)


    @staticmethod
    def getFileDataSets(pth='./', title=None, parent=None):  # pylint: disable=C0103; # pragma: no cover
        """
        Retrieve the filename and datasets selected by the user (via GUI)

        Parameters
        ----------
        pth : str
            Home directory to start in OR the relative pth to a file

        Returns
        ----------
        Tuple (str, str, list[str]) as (path, filename, [dataset(s)])

        """

        # pragma: no cover
        dialog = HdfLoad(title=title, parent=parent)

        ret_fileopen = True
        if pth is None:
            pth = './'
        else:
            pth = _os.path.abspath(pth)

        while True:
            ret_fileopen = dialog.fileOpen(pth, title=title)

            ret = None
            if ret_fileopen:
                ret_dset_select = dialog.exec_()
                if ret_dset_select == _QDialog.Rejected:
                    pth = dialog.path
                elif dialog.all_selected is None:
                    pass
                else:
                    ret = (dialog.path, dialog.filename, dialog.all_selected)
                    break
            else:
                break
        return ret

    def fileOpen(self, pth='./', title=None):  # Qt-related pylint: disable=C0103
        """ Select HDF5 File via QDialog built-in."""

        if pth is None:
            pth = './'

        if title is None:
            title_file='Select a file...'
        else:
            title_file='{}: Select a file...'.format(title)

        if _os.path.isdir(pth):  # No file provided, use QFileDialog; # pragma: no cover
            filetype_options = 'HDF5 Files (*.h5 *.hdf *.hdf5);;All Files (*.*)'
            full_pth_fname, _ = _QFileDialog.getOpenFileName(self, title_file, pth,
                                                             filetype_options)
        elif _os.path.isfile(pth):  # Is a valid file
            full_pth_fname = pth
        else:
            raise FileNotFoundError('Not a valid path. Not a valid file.')

        ret = None
        if full_pth_fname:
            full_pth_fname = _os.path.abspath(full_pth_fname)  # Ensure correct /'s for each OS
            self.filename = _os.path.basename(full_pth_fname)
            self.path = _os.path.dirname(full_pth_fname)
            self.populateGroups()
            ret = True
        return ret

    def populateGroups(self):  # Qt-related pylint: disable=C0103
        """ Populate dropdown box of group ui.comboBoxGroupSelect """
        self.group_dset_dict = get_hierarchy(_os.path.join(self.path, self.filename),
                                             grp_w_dset=HdfLoad.config['only_show_grp_w_dset'])
        # Load Group dropdown box
        self.ui.comboBoxGroupSelect.clear()
        for count in self.group_dset_dict:
            self.ui.comboBoxGroupSelect.addItem(count)
        return [self.path, self.filename]

    def dataGroupChange(self):  # Qt-related pylint: disable=C0103
        """ Action : ComboBox containing Groups with DataSets has changed"""
        self.ui.listDataSet.clear()

        if self.ui.comboBoxGroupSelect.currentText() != '':
            self.ui.listDataSet.addItems(self.group_dset_dict[self.ui.comboBoxGroupSelect.currentText()])
            
            file_name = _os.path.join(self.path, self.filename)
            group_path = self.ui.comboBoxGroupSelect.currentText()
            
            attr_dict = get_attrs_group(file_name, group_path)            
            self.populate_attrs(attr_dict = attr_dict)
                    
        

    def populate_attrs(self, attr_dict=None):
        """ Populate attribute for currently selected group """
        self.ui.tableAttributes.blockSignals(True) #block udpate signals for auto-filled forms
        self.ui.tableAttributes.setRowCount(0)
        self.ui.tableAttributes.setColumnCount(2)
        self.ui.tableAttributes.setSortingEnabled(False)

        if attr_dict:
            for num, key in enumerate(attr_dict):
                self.ui.tableAttributes.insertRow(self.ui.tableAttributes.rowCount())
                key_item = _QTableWidgetItem(key)
                key_item.setFlags( Qt.ItemIsSelectable | Qt.ItemIsEnabled )
                self.ui.tableAttributes.setItem(num, 0, key_item)
                
                val_item = _QTableWidgetItem(str(attr_dict[key]))
                val_item.setFlags( Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled )
                self.ui.tableAttributes.setItem(num, 1, val_item)
                
        self.ui.tableAttributes.blockSignals(False)
        
    def update_attrs_to_file(self, item):
        file_name = _os.path.join(self.path, self.filename)
        group_path = self.ui.comboBoxGroupSelect.currentText()

        attr_key = self.ui.tableAttributes.item(item.row(),0).text()
        attr_val = item.text()

        #update attr in file
        alter.alter_attr(group_path, attr_key, attr_val, file=file_name, pth=None, verbose=False,
                             check_same_type=False, must_exist=False)

            

    def datasetSelected(self):  # Qt-related pylint: disable=C0103
        """ Action : One or more DataSets were selected from the list """

        all_selected = self.ui.listDataSet.selectedItems()
        n_selected = len(all_selected)

        self.ui.textCurrentDataset.setText('')
        self.all_selected = []
        attrs = {}

        if n_selected > 0:
            current_selection = all_selected[-1].text()
            current_grp = self.ui.comboBoxGroupSelect.currentText()

            selection_str = '{} + ({} others)'.format(current_selection, n_selected - 1)
            self.ui.textCurrentDataset.setText(selection_str)
            current_dset_fullpath = '{}/{}'.format(current_grp, current_selection)
            attrs = get_attrs_dset(_os.path.join(self.path, self.filename),
                                   current_dset_fullpath, convert_to_str=True)
            self.all_selected = ['{}/{}'.format(current_grp, selection.text())
                                 for selection in all_selected]

        # Fill-in attribute table
        self.populate_attrs(attr_dict=attrs)

    def filterDatasets(self):  # Qt-related pylint: disable=C0103
        """ Filter list of datasets based on include and exclude strings """
        incl_str = self.ui.filterIncludeString.text()
        excl_str = self.ui.filterExcludeString.text()

        # From string with comma separation to list-of-strings
        incl_list = [q.strip() for q in incl_str.split(',') if q.strip()]
        excl_list = [q.strip() for q in excl_str.split(',') if q.strip()]

        dset_list = [self.ui.listDataSet.item(num).text() for num in
                     range(self.ui.listDataSet.count())]

        if incl_list:  # Include list is not empty
            dset_list = filterlist(dset_list, incl_list,
                                   keep_filtered_items=True,
                                   exclusive=HdfLoad.config['excl_filtering'])

        if excl_list:  # Exclude list is not empty
            dset_list = filterlist(dset_list, excl_list,
                                   keep_filtered_items=False,
                                   exclusive=HdfLoad.config['excl_filtering'])

        self.ui.listDataSet.clear()
        self.ui.listDataSet.addItems(dset_list)

if __name__ == '__main__':  # pragma: no cover
    app = _QApplication(_sys.argv)  # pylint: disable=C0103
    result = HdfLoad.getFileDataSets(pth='.', title='Test title')  # pylint: disable=C0103
    print('Result: {}'.format(result))

    _sys.exit()
    # pylint: error
