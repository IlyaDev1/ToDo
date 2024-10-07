from rest_framework.exceptions import ValidationError


class TaskValidator:
    @staticmethod
    def is_today_valid(is_today: str | None) -> bool | None:
        if is_today:
            if is_today not in ['0', '1']:
                raise ValidationError('u must use is_today=1 or is_today=0')
        return True

    @staticmethod
    def is_tags_valid(tags: str | None) -> bool | None:
        if tags:
            try:
                tags.split(',')
            except Exception:
                raise ValidationError('u must use tag=tag1,tag2,...')
        return True
