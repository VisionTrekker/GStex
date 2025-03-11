import os
from datetime import datetime
from os.path import exists

def get_formatted_time():
    return datetime.now().strftime("%Y-%m-%d_%H%M%S")
time = get_formatted_time()

GPU_ID = 1

# dataset_name = "dtu"
# detailed_log_dir = f"./results/{dataset_name}_nvs/logs"
# os.makedirs(detailed_log_dir, exist_ok=True)
# scene_name = "scan24"
# experiment_name = scene_name + "_nvs"
# # 训练
# cmd = f"ns-train gstex-dtu-nvs \
#         --experiment-name {experiment_name} \
#         --timestamp {time} \
#         --pipeline.model.num-random -1 \
#         --pipeline.model.init-ply /data2/liuzhi/Dataset/3DGS_Dataset/DTU/dtu/{scene_name}/init_nvs/point_cloud.ply \
#         --data /data2/liuzhi/Dataset/3DGS_Dataset/DTU/dtu/{scene_name} \
#         > {detailed_log_dir}/{experiment_name}__{time}_train.log \
#         "
# print(cmd)
# os.system(cmd)

# # 评价
# cmd = f"ns-eval \
#         --load-config ./outputs/{experiment_name}/gstex/{time}/config.yml \
#         --output-path ./renders/{experiment_name}/gstex/{time}/output.json \
#         --render-output-path ./renders/{experiment_name}/gstex/{time}/images \
#         > {detailed_log_dir}/{experiment_name}__{time}_eval.log \
#         "
# print(cmd)
# os.system(cmd)

# 从2DGS的输出的模型中初始化高斯

dataset_name = "reality"
detailed_log_dir = f"./results/{dataset_name}_nvs/logs"
os.makedirs(detailed_log_dir, exist_ok=True)

# scene_name = "gm_Museum"    # /data2/liuzhi/remote_data/result/liuzhi/2DGS/{scene_name}_0.1gtdepthnormal/point_cloud/iteration_30000/point_cloud.ply
# scene_name = "memorial4"  # /data2/liuzhi/remote_data/result/liuzhi/2DGS/{scene_name}_0.05gtnormal_gtsurfel_0.1gtdepth/point_cloud/iteration_30000/point_cloud.ply
scene_name = "copybook"   # /data2/liuzhi/remote_data/result/liuzhi/2DGS/2copybook_nodensify_nofixnormal/point_cloud/iteration_30000/point_cloud.ply

cmd = f"CUDA_VISIBLE_DEVICES={GPU_ID} \
        ns-train gstex \
        --data /data2/liuzhi/Dataset/3DGS_Dataset/input/{scene_name} \
        --pipeline.model.init-ply /data2/liuzhi/remote_data/result/liuzhi/2DGS/{scene_name}_0.1gtdepthnormal/point_cloud/iteration_30000/point_cloud.ply \
        --pipeline.model.fix-init True \
        \
        "
print(cmd)
os.system(cmd)

# 评价
cmd = f"CUDA_VISIBLE_DEVICES={GPU_ID} \
        ns-eval \
        --load-config ./outputs/{scene_name}/gstex/{time}/config.yml \
        --output-path ./renders/{scene_name}/gstex/{time}/output.json \
        --render-output-path ./renders/{scene_name}/gstex/{time}/images \
        > {detailed_log_dir}/{scene_name}__{time}_eval.log \
        "
print(cmd)
os.system(cmd)