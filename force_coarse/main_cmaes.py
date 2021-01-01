import numpy as np
import optuna
import matlab.engine
import time
import scipy.io as scio

n_trails = 2000
study_name = 'cmaes'
storage = 'sqlite:///cmaes.db'


names = matlab.engine.find_matlab()
engs = []
for name in names:
    engs.append(matlab.engine.connect_matlab(name))
num_worker = len(names)
time_start=time.time()
eng=engs[0]

# define study (the job for each worker)

def objective(trial):
    variables=[]
    for i in range(25):
        variable=trial.suggest_uniform(f'var{i}', 0.,1.)
        variables.append(float(variable))
    energy=eng.func_python_api(variables)

    # energy=np.std(np.array(variables))
    return energy
    


if __name__ == '__main__':
    if num_worker==0:
        print('Error: no Matlab worker detected')
    else:
        print('Number of worker(s): {:d}'.format(num_worker))

    try:
        optuna.study.delete_study(study_name, storage)
    except:
        pass

    study = optuna.create_study(study_name=study_name,
                                storage=storage,
                                direction='minimize',
                                sampler=optuna.samplers.CmaEsSampler(seed=0)
                                )
    study.optimize(objective, n_trials=n_trails)
    y_list=optuna.visualization.plot_optimization_history(study)['data'][0]['y']
    scio.savemat('data_cmaes.mat',{'y': y_list})


