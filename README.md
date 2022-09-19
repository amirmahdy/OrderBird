# Repository Evaluator 

This application is aimed to evaluate the popularity of a GitHub repository using GitHub Rest API. To gain access to private repositories Token is going to be used.

The application tech stacks are as follows.

Python, Django, PostgreSQL, Nginx, Docker.

## Considerations
This application assumes that the user saves the Tokens in DB for accessing private repositories. 
By doing this the redundancy to repeat the token and security issues are reduced.
This application for gathering edge cases requires a log manager (SPLUNK).


## Installation

To install the application use the following commands.

```bash
sudo make build
sudo make start
```
Other make commands are, stop, down and restart.
## API Reference

The swagger interface is accessible on http://127.0.0.1/swagger/
### Popularity

```http
  GET /popularity
```
This endpoint evaluates the popularity of a repository based on the number of forks and stars.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `owner` | `string` | **Required**. Owner of the repository |
| `repo` | `string` | **Required**. Repository name |



### Repository endpoints
```http
  GET /repository
```
This endpoint returns all repositories on the DB.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |

```http
  POST /repository
```
This endpoint saves a repository on the DB.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `owner` | `string` | **Required**. Owner of the repository |
| `repository` | `string` | **Required**. Repository name |
| `token` | `int` | **Optional**. Token id |

```http
  PATCH /repository
```
This endpoint modifies a repository token on the DB.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `owner` | `string` | **Required**. Owner of the repository |
| `repository` | `string` | **Required**. Repository name |
| `token` | `int` | **Optional**. Token id |



### Token endpoints
```http
  GET /token
```
This endpoint returns all token names on the DB.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |

```http
  POST /repository
```
This endpoint saves a token on the DB.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | **Required**. Owner of the repository |
| `token` | `string` | **Required**. Token value |


### Admin endpoints
This page is accessible from http://127.0.0.1/admin. 

This page navigates the admin through DB and shows elements on the DB.
This page requires user credentials which by default are (admin, 123456).

### HealthCheck endpoints
This page is accessible from http://127.0.0.1/health_check. 

This endpoint evaluates cache, DB, storage, and migration. This endpoint is using a third-party library [django-health-check](https://django-health-check.readthedocs.io/en/latest/)

## Final Note
There are some things that can be upgraded in the future.

Most importantly encrypting the Token is important for safer storage, using Django secret key.

Searching over GitHub repository, using https://api.github.com/search/repositories?q=OrderBird
