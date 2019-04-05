import os, numpy as np
from ..idtrackerai_importer import import_idtrackerai_project

class IdTrackerProject(object):


    def load(self, data, project_path=None):
        """
        Check if the the path includes an idtrackerai project, if so load it.
        :param data:
        :param project_path:
        :return:
        """
        blobs_path  = os.path.join(project_path, 'preprocessing', 'blobs_collection_no_gaps.npy')
        vidobj_path = os.path.join(project_path, 'video_object.npy')

        if os.path.exists(blobs_path) and os.path.exists(vidobj_path):

            """
            import_idtrackerai_project(
                self,
                project_path,
                progress_event=self.__update_progress_evt
            )
            """

            v = np.load(vidobj_path).item()
            video = self.create_video()
            video.filepath = os.path.join(project_path, '..', os.path.basename(v._video_path))

            obj = video.create_idtrackerai_object()
            obj.path = blobs_path

            return data
        else:
            return super().load(data, project_path)


    def __update_progress_evt(self, progress_count, max_count=None):
        progress = self.mainwindow.progress_bar

        if max_count is not None and progress_count==0:
            progress.max = max_count
            progress.value = 0
            progress.show()
        elif progress.max == progress_count:
            progress.hide()
        else:
            progress.value = progress_count