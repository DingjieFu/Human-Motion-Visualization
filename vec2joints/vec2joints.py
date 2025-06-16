import torch
import argparse
import numpy as np
from os.path import join as pjoin
from common.plot_script import plot_3d_motion
from common.motion_process import recover_from_ric
from common.paramUtil import *


parser = argparse.ArgumentParser()
parser.add_argument('--dataset_name', default="t2m", help='[t2m, kit]')
parser.add_argument('--vec_name', default="000000")
parser.add_argument('--save_dir', default="/root/project/MotionVis/vec2joints/demo/joints")
parser.add_argument('--is_save', action="store_true")
opt = parser.parse_args()


def inv_transform(data, std, mean):
    return data * std + mean


if opt.dataset_name == "t2m":
    data_root = '/root/project/datasets/HumanMotion/HumanML3D/'
    joints_num = 22
    fps = 20
    radius = 4
    kinematic_chain = t2m_kinematic_chain
elif opt.dataset_name == "kit":
    data_root = '/root/project/datasets/HumanMotion/KIT-ML/'
    joints_num = 21
    radius = 240 * 8
    fps = 12.5
    kinematic_chain = kit_kinematic_chain
else:
    raise KeyError('Dataset Does not Exists')

# mean, std = np.load(pjoin(data_root, 'Mean.npy')), np.load(pjoin(data_root, 'Std.npy'))

data = np.load(f"./demo/vecs/{opt.vec_name}.npy")


# joint_data = inv_transform(data, std, mean)
joint_data = data
joint = recover_from_ric(torch.from_numpy(joint_data).float(), joints_num).numpy()
print(joint.shape)

save_path = opt.save_dir + f"/{opt.vec_name}_joints.mp4"
plot_3d_motion(save_path, kinematic_chain, joint, title="None", fps=fps, radius=radius)

# if opt.is_save:
#     save_path = opt.save_dir + f"/{opt.vec_name}_joints.npy"
#     np.save(save_path, joint)
