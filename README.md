# FSND Capstone Project
This application is created as part of the capstone project for capstone, last of Udacity's Full-stack nanodegree projects.
The project models a Casting Agency company that is responsible for creating movies and casting actors.

###The application is running on: https://njoud-fsnd.herokuapp.com/

This application provides the following:
- viewing all listed actors and movies registered by the company.
- adding a movie or an actor profile.
- delete a movie or an actor profile.
- modifying a movie or an actor's info.

### The API allows 3 levels of authorization: 

#### Public: 
- can view all listed Movies
- can view all listed Actors

#### Casting Director:
- can view listed movies and actors
- can add or delete an actor from the DB
- can modify a movie data in the DB

#### Executive Producer:
- can view listed movies and actors
- can add or delete an actor from the DB 
- can add or delete a movie from the DB 
- can modify an actor or movie data in the DB

### Getting Started
Installing dependencies:

```bash
pip install -r requirements.txt
```

### Running the server

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
### Testing
To run the tests, run
```
python test_app.py
```

## API Reference
Base URL: The API is hosted on: https://njoud-fsnd.herokuapp.com/

####Authentication: 
authentication is required for accessing endpoint with POST, DELETE, or PATCH methods.
- executive_producer_token
```
Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxHMlFGZ2NHQmM5cGxQcTdzbjBpWSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbmpvdWQudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMDVkZGY3ZDkzZmRkMDA2ZmFjY2U3OCIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTYxNDA5MzExNiwiZXhwIjoxNjE0MTc5NDE2LCJhenAiOiI5Sng3b2E1cXRSbDdEUm12NnV4eHUyN2RBUGIxVEJkeCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.IK1uqbhoiG5pMEaPtsH8fg37wCkeIWa5Fn0OJszIZanOgW-piL6aLBTwg0SDXNFrlDKvQ8r9kxCsrAoCeYBiTgyrc9KwsZfbx0cZZGIwniSpTuY5skeb3iXm8lvJJ_cC49KflVJSs4y_AN9lAEtMZ_3lUBnDesMlXRmFrxyHYVMB29rAXe53065zEQjuKaLh5lF-U9aGMLCTI9A23jcgll-f9j6Kk_fGqRlgQyKXgO2K8ocQur5U4KrAZ0_Kvq4ukT5ds9GRYdsJEF2zLbR6-hRUUy3-622t_XDytN38dPJmv7mOdcioEmTEj2phpZ8qwvXtI0eLCQn-KvLLeJEE0g
```
- casting_director_token
```
Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxHMlFGZ2NHQmM5cGxQcTdzbjBpWSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbmpvdWQudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMDVkZjYwMzIyNWY5MDA3N2NmZmQyZSIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTYxNDA5MzI0MCwiZXhwIjoxNjE0MTc5NTQwLCJhenAiOiI5Sng3b2E1cXRSbDdEUm12NnV4eHUyN2RBUGIxVEJkeCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.dt5bM67Rk6JaE8apiUKmKpmAfBhCu5H_SpzsjV08hT08kSnzVeTNrHACssjCaVckXg3YdUuUuMSEjztGpKXLpbMlNCzadmO3U1Tex8pZQI4ZgplNFRJ01opugH5u8JToJ-GGYpX2WATFaVn8ExdSZKAoXwGR4H7lVRXGBOP0GSm3aEJyXKGhKA6hddewIBiwfiOyWyMqnsawZ6O4l8IOFWht8DyGiDWmIkxZXi73wOVxeXpVSpGWaJ07swHYDiUjI97ByLaOtknVv7rcqmCXvhuC8hFLbDAP5P5g--T_GxsR3EQRu1C5eOhLSUDxdgpG1Mj-yDjkKZgFo-2B6pRbpA
```

### Error handling
The API will return one of the following errors if a request fails:

- 400 – bad request
- 404 – result not found
- 422 – un-processable
- 401 - un-authorized

in case of failure, error response will be returned as JSON in the following format:
```
{
    "success": False,
    "error": 400,
    "message": "bad request"
}
```
### Endpoints
#### GET /actors
This endpoint returns all listed actors from the db.

sample request ```curl https://njoud-fsnd.herokuapp.com/actors```

#### GET /movies
This endpoint returns all listed movies from the db.

sample request ```curl https://njoud-fsnd.herokuapp.com/movies```

#### POST /actors
This endpoint allows inserting new actor info to the db. 
*accessible only by user with Casting Director or Executive Producer privilege.

sample request ```curl -X POST https://njoud-fsnd.herokuapp.com/actors -d '{"name": "njoud", "gender": "female", "age": 25}' -H "Content-Type: application/json, Authorization: Bearer <token>"```

#### POST /movies
This endpoint allows inserting new actor info to the db. 
*accessible only by user with only Executive Producer privilege.

sample request ```curl -X POST https://njoud-fsnd.herokuapp.com/movies -d '{"title": "FSND", "release_date": "2023-05-05"}' -H "Content-Type: application/json, Authorization: Bearer <token>"```

#### DELETE /actors/< int:actor_id>
This endpoint fulfills the deletion of and actor listed from database based on an actor's id.
*accessible only by user with Casting Director or Executive Producer privilege.

sample request ```curl -X DELETE https://njoud-fsnd.herokuapp.com/actors/1```

#### DELETE /movies/< int:movie_id>
This endpoint fulfills the deletion of and actor listed from database based on an actor's id.
*accessible only by user with only Executive Producer privilege.

sample request ```curl -X DELETE https://njoud-fsnd.herokuapp.com/movies/1```

#### PATCH /actors/< int:actor_id>
This endpoint allows modifying data of listed actor from the database based on an actor's id.
*accessible only by user with Casting Director or Executive Producer privilege.

sample request ```curl -X PATCH https://njoud-fsnd.herokuapp.com/actors/1 -d '{"age": 27}' -H "Content-Type: application/json, Authorization: Bearer <token>"```

#### PATCH /movies/< int:movie_id>
This endpoint allows modifying data of listed movie from the database based on an actor's id.
*accessible only by user with only Executive Producer privilege.

sample request ```curl -X PATCH https://njoud-fsnd.herokuapp.com/movies/1 -d '{"title": "DAND"}' -H "Content-Type: application/json, Authorization: Bearer <token>"```
