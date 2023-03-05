using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace miles_to_km_converter
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private Double get_coefficient()
        {
            if (label3.Text=="Mile")
            {
                return 1.609344;
            }
            else
            {
                return 0.6213711922;
            }
        }
        private void label1_Click(object sender, EventArgs e)
        {
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }
        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }
        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }
        private void button3_Click(object sender, EventArgs e)
        {
            label3.Text = "Mile";
            label4.Text = "Kilometer";
            textBox1.Text = "";
            textBox2.Text = "";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double coefficient = get_coefficient();
            double  textbox_value;
            try
            {
                textbox_value = Convert.ToDouble(textBox1.Text);
                textBox2.Text = Convert.ToString(coefficient * Convert.ToDouble(textBox1.Text));
            }
            catch (Exception)
            {
                MessageBox.Show(textBox1.Text+" is not a number","Error",MessageBoxButtons.OK,MessageBoxIcon.Error );
            }   
        }

        private void button2_Click(object sender, EventArgs e)
        {
            String label=label3.Text;
            label3.Text=label4.Text;
            label4.Text = label;
            textBox1.Text = "";
            textBox2.Text = "";
        }
    }
}
