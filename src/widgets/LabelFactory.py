import const.app_config as AppConfig

from widgets.CustomLabel import CustomLabel
from widgets.TitleLabel import TitleLabel

class LabelFactory:
    def getLabel(self, label_type, parent, text, color=None):
        if label_type == AppConfig.LABEL_NORMAL:
            return CustomLabel(parent, text, color)
        elif label_type == AppConfig.LABEL_TITLE:
            return TitleLabel(parent, text)
        else:
            return None