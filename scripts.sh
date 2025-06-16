# ---------- 1. joints ani ---------- #
# visualize stick gifs
### conda activate movis
cd /joints_ani
python animation.py 


# ---------- 2. joints2smpl ---------- #
# generates .ply files -> [blender]
### conda activate movis
cd /jointssmpl
python fit_seq.py --gpu_ids 0


# ---------- 3. smpl render ---------- #
# generates smpl gifs(mp4) and png
### conda activate movis
cd /smpl_render
python render_final.py --filedir /smpl_render/demo/ --motion-list sample0_repeat0_len196


# ---------- 4. vec2joints ---------- #
# new_joint_vecs -> new_joints
### conda activate movis
cd /vec2joints
python vec2joints.py --vec_name 000000 --is_save