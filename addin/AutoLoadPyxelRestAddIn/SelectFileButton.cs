using System;
using System.Windows.Forms;

namespace AutoLoadPyxelRestAddIn
{
    public class SelectFileButton: PictureBox
    {
        public SelectFileButton()
        {
            Image = Properties.Resources.add_file_16;
            Padding = new Padding(0, 4, 0, 0);
            Width = 20;
            Height = 30;
            MouseEnter += SelectFileButton_MouseEnter;
            MouseLeave += SelectFileButton_MouseLeave;
        }

        private void SelectFileButton_MouseEnter(object sender, EventArgs e)
        {
            Image = Properties.Resources.file_4_16;
        }

        private void SelectFileButton_MouseLeave(object sender, EventArgs e)
        {
            Image = Properties.Resources.add_file_16;
        }
    }
}
