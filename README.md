# CS269 (Robustness of Multi-modal Transformers using Visual Question Generation)


# Preparing Environment:

`conda create -n pytorch1.5 python=3.6`

`source activate pytorch1.5`

`conda install pytorch=1.5 torch torchvision numpy transformers tqdm`

`conda install -c conda-forge ipython jupyter ipywidgets`

`python -m ipykernel install --user --name=pytorch1.5`

# VQG Training using COCO data

We use the transformer implementation from https://github.com/saahiluppal/catr as our VQG model

Train VQG using the below command:

 `python main.py`
 
 Please make sure that you download COCO dataset into the data folder before launching training. (See https://github.com/arjunakula/catr for more details on Data Preparation)

# VQG Inference and Qualitative Anslysis

You can direclty run the jupyter notebook 'CS269_demo2.ipynb' to infer and perform qualitative analysis

# Sample Generation Output

Please see the data in the folder 'OOD_data'

# Converting Caption Output from VQG to Question using our Rule-based Approach

`cd practNLPTools-1.0/`

Install practNLP dependencies by running setup.py and then run the below command

`python convert_caption_to_question.py input_captions.txt output_captions.txt`

# VQA Robustness Analysis using OOD split

Install ViLBERT code using my repository here: https://github.com/arjunakula/vilbert_beta

(Please do not use original implementation as it is not designed for contrastive losses and multi-task learning. I have made few changes to easily run multi-task learning)

Replace the task_utils.py with the file in this repository 'train_tasks_MTL_gqa_rel'. And then follow ViLBERT instructions to train and test VQA model.

