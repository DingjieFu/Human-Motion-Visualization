<div align="center">
<h1> Human-Motion-Visualization </h1>
</div>

## Overview

This repository provides ***four*** methods for visualizing human motion data (e.g., the HumanML3D dataset), they are:

- joints animation : convert joint position data into a **stick-figure animation**
- vector to joints: convert rotation invariant feature to 3D motion positions
- joints to SMPL:  convert joint position data into **ply files**
- SMPL render: render SMPL from joints

## Getting Started

<h3> • Requirements </h3>

```
git clone git@github.com:DingjieFu/Human-Motion-Visualization.git
cd Human-Motion-Visualization
conda env create -f environment.yml
```

<h3> • Data Preparation </h3>

The datasets ([HumanML3D](https://github.com/EricGuo5513/HumanML3D), [KIT-ML](https://github.com/EricGuo5513/HumanML3D)) are publicly accessible.

