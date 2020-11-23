using System;
using System.Windows.Forms;

namespace PyxelRestAddIn
{
    internal class DeleteButton: PictureBox
    {
        public DeleteButton(int width)
        {
            Image = Properties.Resources.x_mark_3_16;
            Padding = new Padding(0, 4, 0, 0);
            Width = width;
            MouseEnter += DeleteButton_MouseEnter;
            MouseLeave += DeleteButton_MouseLeave;
        }

        private void DeleteButton_MouseEnter(object sender, EventArgs e)
        {
            Image = Properties.Resources.x_mark_4_16;
        }

        private void DeleteButton_MouseLeave(object sender, EventArgs e)
        {
            Image = Properties.Resources.x_mark_3_16;
        }
    }
}
