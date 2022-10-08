## Discovering and Achieving Goals via World Models

####  [[Project Website]](https://orybkin.github.io/lexa/) [[Benchmark Code]](https://github.com/orybkin/lexa-benchmark) [[Video (2min)]](https://www.youtube.com/watch?v=LnZj2lZYD3k) [[Oral Talk (13min)]](https://www.youtube.com/watch?v=WWHlQbigQp4) [[Paper]](https://arxiv.org/pdf/2110.09514.pdf)
[Russell Mendonca](https://russellmendonca.github.io/)\*<sup>1</sup>, [Oleh Rybkin](https://www.seas.upenn.edu/~oleh/)\*<sup>2</sup>, [Kostas Daniilidis](http://www.cis.upenn.edu/~kostas/)<sup>2</sup>, [Danijar Hafner](https://danijar.com/)<sup>3,4</sup>, [Deepak Pathak](https://www.cs.cmu.edu/~dpathak/)<sup>1</sup><br/>
(&#42; equal contribution, random order)

<sup>1</sup>Carnegie Mellon University </br> 
<sup>2</sup>University of Pennsylvania </br>
<sup>3</sup>Google Research, Brain Team </br> 
<sup>4</sup>University of Toronto </br> 

<img src="https://russellmendonca.github.io/data/lexa-method.gif" width="600">

Official implementation of the [Lexa](https://orybkin.github.io/lexa/) agent from the paper Discovering and Achieving Goals via World Models.

## Setup

### Clone
Clone this repo and the [lexa-benchmark](https://github.com/orybkin/lexa-benchmark) repo to a directory. If cloning these repositories using command line yield any errors, make sure to just download the zip folder for them.

```
git clone https://github.com/balloch/lexa.git
git clone https://github.com/orybkin/lexa-benchmark
```

### Install Dependencies
If GLEW is not already installed, install it using `sudo apt-get install libglew-dev`. Also install the following libraries for mujoco: `sudo apt install libosmesa6-dev libgl1-mesa-glx libglfw3 patchelf`.

### Setup Mujoco

Use [this link](https://www.roboti.us/download/mujoco200_linux.zip) to download mujoco200 for linux and unzip the folder into `~/.mujoco/mujoco200`

Then put the activation key from [this link](https://www.roboti.us/file/mjkey.txt) into the this directory: `~/.mujoco/`

### Setup Env Variables

Add the following lines to the `~/.bashrc` file:

```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/.mujoco/mujoco200/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/nvidia

export PYTHONPATH=<path to lexa repo>/lexa:<path to lexa-benchmark repo>

export MUJOCO_RENDERER=egl; export MUJOCO_GL=egl
export MJLIB_PATH=~/.mujoco/mujoco200/bin/libmujoco200.so
export MJKEY_PATH=~/.mujoco/mjkey.txt

export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so
```

This will setup library paths, python path, mujoco paths, and mujoco rendering variables. Then restart your terminal or run `source ~/.bashrc`. Note that the path to nvidia (/usr/lib/nvidia) might be in a different place. For example, /usr/lib/nvidia-460.

### Setup Conda environment
Create the conda environment by running : 

```
conda env create -f environment.yml
conda activate lexa
```

### Install MiniGrid
Install the mini grid environment using:

```
pip install gym-minigrid
```

### Troubleshooting

If this error comes up:
```
libstdc++.so.6: version `GLIBCXX_3.4.29' not found
```

try a solution similar to the one in [this link](https://github.com/pybind/pybind11/discussions/3453)

**WARNING!** Make sure to use the right python and mujoco version. The robobin environment code is known to break with other versions. Other environments might or might not work.

## Training

First source the environment : `conda activate lexa`

For training, run : 

```
export CUDA_VISIBLE_DEVICES=<gpu_id>  
python train.py --configs defaults <method> --task <task> --logdir <log path>
```
where method can be `lexa_temporal`, `lexa_cosine`, `ddl`, `diayn` or `gcsl`   
Supported tasks are `dmc_walker_walk`, `dmc_quadruped_run`, `robobin`, `kitchen`, `joint`

To view the graphs and gifs during training, run `tensorboard --logdir <log path>`

Example:
```
python train.py --configs defaults lexa_temporal --task dmc_walker_walk --logdir ~/logdir/lexa_temporal_walker
```
or on a minigrid environment
```
python train.py --configs defaults lexa_temporal --task MiniGrid-DoorKey-8x8-v0 --logdir ~/logdir/lexa_minigrid
```

## Bibtex
If you find this code useful, please cite:

```
@misc{lexa2021,
    title={Discovering and Achieving Goals via World Models},
    author={Mendonca, Russell and Rybkin, Oleh and
    Daniilidis, Kostas and Hafner, Danijar and Pathak, Deepak},
    year={2021},
    Booktitle={NeurIPS}
}
```

## Acknowledgements
This code was developed using [Dreamer V2](https://github.com/danijar/dreamerv2) and [Plan2Explore](https://github.com/ramanans1/plan2explore).
