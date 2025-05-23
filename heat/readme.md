# Heat enhancement problem with 10x10 variables

## Software environment

* COMSOL Multiphysics 5.4
* Matlab 2019b
* Python 3.7
    * PyTorch 1.2.0

> [!CAUTION]
> Some users with COMSOL 6.0 or higher reported error when running the MPH file. (In MATLAB, it will report "calculation failed" and you can check "commandOut" variable to confirm it's a COMSOL error). I suggest using 5.4 or modify the model towards your needs instead of trying to replicate the results. 

## Code

* <strong>heat.m</strong>: MATLAB script to generate a COMSOL file, used to calculate charging time based on given density distribution
* <strong>heat_approx.m</strong>: MATLAB script to generate a COMSOL file, used to calculate optimal configuration based on MMA ("Approximated" method
  in the paper)

* <strong>func_*.m</strong>: MATLAB function scripts
    * <strong>func_inputs_gen.m</strong>: a function to generate input data, i.e., $\rho$ in paper
    * <strong>func_outputs.m</strong>: a function to calculate output, i.e., reciprocal of charging time, 1/t
    * <strong>func_outputs_par.m</strong>: a function to calculate output, a parallel version of <strong>func_outputs.m</strong>
    * <strong>func_outputs_withgrad_par.m</strong>: a function to calculate output and its gradient w.r.t design variables, with parallel computing
    * <strong>func_test.m</strong>: a function to evaluate the optimized solution $\hat{\rho}$ from DNN
    * Others are used to plot

* <strong>main_*.m</strong>: MATLAB code to generate data
    * <strong>main_solo.m</strong>: code to implement our proposed SOLO algorithm, and generate data in subfolder "data_solo"
    * <strong>main_direct.m</strong>: code to implement "Direct" algorithm, and generate data in "data_direct.mat"


* <strong>plot_*.m</strong>: MATLAB code to plot the data
    * <strong>plot_b.m</strong>: plot figure b
    * <strong>plot_c_d_e.m</strong>: plot figures c, d, and e
    * <strong>plot_s7.m</strong>: plot Supplementary Figure 7


* <strong>mlopt.py</strong>: (abbreviation of Machine Learning and OPTimization) python code to train a Deep Learning Network (DNN) and obtain the
  optimized solution based on the DNN by Bat Algorithm (BA)
* <strong>ba.py</strong>: python function for Bat Algorithm (BA)

## Data

If you run the code, data will be generated and stored in subfolders:

* <strong>data_solo</strong>: data generated by the code "main_solo.m" for SOLO

You will also get a file:

* <strong>data_direct.mat</strong>: data generated by "main_direct.m" for "Direct" method

Data is not uploaded to Github. Please download
from [Google Drive](https://drive.google.com/drive/folders/1f6Xrd9e-RAUsh9vqIqUXbEw8F1_2Qg_5?usp=sharing) or email us.

## How to run

1. Connect MATLAB with COMSOL server
2. Run __heat.m__ by COMSOL to generate __heat.mph__, or download it
   from [Google Drive](https://drive.google.com/drive/folders/1f6Xrd9e-RAUsh9vqIqUXbEw8F1_2Qg_5?usp=sharing)
3. Run __main_solo.m__ and __main_direct.m__
4. Run __heat_approx.m__ by COMSOL to generate __heat_approx.mph__, or download it
   from [Google Drive](https://drive.google.com/drive/folders/1f6Xrd9e-RAUsh9vqIqUXbEw8F1_2Qg_5?usp=sharing)
5. [optional] Run __plot_b.m__ and __plot_s7.m__
6. [optional] Run __plot_c_d_e.m__

As long as a __*.m__ file says `Comsol server required` in the comment at the top, you need to connect the MATLAB with a COMSOL server to run the
file. I recommend adding parameters `-autosave off -np 1 -multi on` (`-autosave off` turns off autosave, `-np 1` sets number of CPU cores of each
server to 1, and
`-multi on` keeps the server after disconnecting COMSOL from MATLAB). You could add to target if you use Shortcut to start the server or to the
command if using command line to start.
