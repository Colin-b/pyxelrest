using System;
using System.Windows.Forms;

namespace PyxelRestAddIn
{
    public class AddButton: PictureBox
    {
        public AddButton(int width)
        {
            Image = Properties.Resources.plus_4_16_grey;
            Padding = new Padding(0, 4, 0, 0);
            Width = width;
            Enabled = false;
            MouseEnter += AddButton_MouseEnter;
            MouseLeave += AddButton_MouseLeave;
            EnabledChanged += AddButton_EnabledChanged;
        }

        private void AddButton_EnabledChanged(object sender, EventArgs e)
        {
            if (Enabled)
                Image = Properties.Resources.plus_4_16;
            else
                Image = Properties.Resources.plus_4_16_grey;
        }

        private void AddButton_MouseEnter(object sender, EventArgs e)
        {
            if (Enabled)
                Image = Properties.Resources.plus_5_16;
        }

        private void AddButton_MouseLeave(object sender, EventArgs e)
        {
            if (Enabled)
                Image = Properties.Resources.plus_4_16;
        }
    }
}
