import dtlpy as dl
import shutil
#please login to kamleshlovesu@gmail.com and password is (studio45#) to access dataloop login and password. 
#run python3 task.py to copy image from source dataset to target dataset.
dl.login()

project = dl.projects.create(project_name='face-detection')
dataset = project.datasets.create(dataset_name='Humans')

project = dl.projects.get(project_name='face-detection')
dataset = project.datasets.get(dataset_name='Humans')

labels = [{'tag': 'people', 'color': (1, 1, 1)}]
dataset.add_labels(label_list=labels)
dataset.items.upload(local_path=r'/home/mspl/Downloads/ai_images',remote_path='/human_face-folder')
filters = dl.Filters(field='real_00034.jpg', values='/little_boy.jpg')

# filters = dl.Filters(field='dir', values='/input')
# trigger = service.triggers.create(function_name='run',
#                                   resource=dl.TriggerResource.ITEM,
#                                   actions=dl.TriggerAction.CREATED,
#                                   name='items-created-trigger',
#                                   filters=filters)

# trigger = service.triggers.create(function_name='run',
#                                   resource=dl.TriggerResource.ITEM,
#                                   actions=dl.TriggerAction.UPDATED,
#                                   name='items-updated-trigger')



original = r'/home/mspl/Downloads/ai_images/source_data/'
target = r'/home/mspl/Downloads/ai_images/target_data/'

#shutil.copyfile(original, target)

import shutil
import os

source_dir = original
target_dir = target
imageNames = ['easy_104_1000.jpg', 'easy_106_0011.jpg']
for imageName in imageNames:
    shutil.copy(os.path.join(source_dir, imageName), target_dir)