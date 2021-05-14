# FLStudy

### Freelance platform for students.

---

## Endpoints for Authorization

#### URL: `api/auth/jwt/create/`

_Use this endpoint to obtain JWT._

| Method | Request                            | Response                                                                                    |
| :----: |:---------------------------------- | :------------------------------------------------------------------------------------------ |
| POST   | <li>username</li><li>password</li> | HTTP_200_OK <li>access</li><li>refresh</li> HTTP_401_UNAUTHORIZED <li>non_field_errors</li> |

#### URL: `api/auth/jwt/refresh/`

_Use this endpoint to refresh JWT._

| Method | Request          | Response                                                                    |
| :----: |:---------------- | :-------------------------------------------------------------------------- |
| POST   | <li>refresh</li> | HTTP_200_OK <li>access</li> HTTP_401_UNAUTHORIZED <li>non_field_errors</li> |


## Endpoints for Tasks

#### URL: `api/task/`

_Use this endpoint to get open tasks or create task._

| Method | Request                                                            | Response                                                                                                                                                    |
| :----: |:------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GET    | <center>-</center>                                                 | HTTP_200_OK                                                                                                                                                 |
| POST   | <li>category</li><li>title</li><li>description</li><li>reward</li> | HTTP_201_CREATE <li>status</li><li>category</li><li>title</li><li>description</li><li>reward</li><li>owner</li><li>date_creation</li> HTTP_401_UNAUTHORIZED |

#### URL: `api/task/<pk>`

_Use this endpoint for task-specific activities._

| Method   | Request                                                            | Response                                                                                                                                                      |
| :------: |:------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| DELETE   | <center>-</center>                                                 | HTTP_204_NO_CONTENT <br> HTTP_401_UNAUTHORIZED                                                                                                                |
| GET      | <center>-</center>                                                 | HTTP_200_OK <li>status</li><li>category</li><li>title</li><li>description</li><li>reward</li><li>owner</li><li>date_creation</li><li>answers (for owner)</li> |
| PUT      | <li>category</li><li>title</li><li>description</li><li>reward</li> | HTTP_200_OK <li>status</li><li>category</li><li>title</li><li>description</li><li>reward</li><li>owner</li><li>date_creation</li> HTTP_401_UNAUTHORIZED       |
