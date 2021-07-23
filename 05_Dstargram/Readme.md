# models.py

### 장고의 기본 유저 모델
```python
from django.contrib.auth.models import User
```
## model field
- ForeignKey(외래키)
    - User 테이블에서 해당 유저를 찾을 수 있는 키
- PrimaryKey(주키)
    - User 테이블에 1 admin 