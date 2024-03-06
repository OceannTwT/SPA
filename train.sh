MASTER_PORT=$(shuf -n 1 -i 10000-65535)

deepspeed --num_gpus=8 --master_port $MASTER_PORT src/train_bash.py \
    --deepspeed deepspeed.json \
    --stage sft \
    --model_name_or_path /mnt/task_runtime/llama/llama-7b \
    --do_train \
    --dataset alpaca_en \
    --finetuning_type full \
    --output_dir /mnt/task_runtime/output6 \
    --overwrite_cache \
    --per_device_train_batch_size 8 \
    --gradient_accumulation_steps 1 \
    --lr_scheduler_type cosine \
    --logging_steps 10 \
    --save_steps 7000 \
    --learning_rate 2e-4 \
    --num_train_epochs 1.0 \
    --adapter_len 32 \
    --plot_loss \
    --fp16