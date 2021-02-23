import os
import unittest
import json
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from app import create_app
from database.models import db_drop_and_create_all, setup_db, Movie, Actor

executive_producer_token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxHMlFGZ2NHQmM5cGxQcTdzbjBpWSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbmpvdWQudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMDVkZGY3ZDkzZmRkMDA2ZmFjY2U3OCIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTYxNDA5MzExNiwiZXhwIjoxNjE0MTc5NDE2LCJhenAiOiI5Sng3b2E1cXRSbDdEUm12NnV4eHUyN2RBUGIxVEJkeCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.IK1uqbhoiG5pMEaPtsH8fg37wCkeIWa5Fn0OJszIZanOgW-piL6aLBTwg0SDXNFrlDKvQ8r9kxCsrAoCeYBiTgyrc9KwsZfbx0cZZGIwniSpTuY5skeb3iXm8lvJJ_cC49KflVJSs4y_AN9lAEtMZ_3lUBnDesMlXRmFrxyHYVMB29rAXe53065zEQjuKaLh5lF-U9aGMLCTI9A23jcgll-f9j6Kk_fGqRlgQyKXgO2K8ocQur5U4KrAZ0_Kvq4ukT5ds9GRYdsJEF2zLbR6-hRUUy3-622t_XDytN38dPJmv7mOdcioEmTEj2phpZ8qwvXtI0eLCQn-KvLLeJEE0g'
casting_director_token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxHMlFGZ2NHQmM5cGxQcTdzbjBpWSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbmpvdWQudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMDVkZjYwMzIyNWY5MDA3N2NmZmQyZSIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTYxNDA5MzI0MCwiZXhwIjoxNjE0MTc5NTQwLCJhenAiOiI5Sng3b2E1cXRSbDdEUm12NnV4eHUyN2RBUGIxVEJkeCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.dt5bM67Rk6JaE8apiUKmKpmAfBhCu5H_SpzsjV08hT08kSnzVeTNrHACssjCaVckXg3YdUuUuMSEjztGpKXLpbMlNCzadmO3U1Tex8pZQI4ZgplNFRJ01opugH5u8JToJ-GGYpX2WATFaVn8ExdSZKAoXwGR4H7lVRXGBOP0GSm3aEJyXKGhKA6hddewIBiwfiOyWyMqnsawZ6O4l8IOFWht8DyGiDWmIkxZXi73wOVxeXpVSpGWaJ07swHYDiUjI97ByLaOtknVv7rcqmCXvhuC8hFLbDAP5P5g--T_GxsR3EQRu1C5eOhLSUDxdgpG1Mj-yDjkKZgFo-2B6pRbpA'


class CastingAgencyTest(unittest.TestCase):
    """This class represents the casting agency test case"""

    '''def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.database_path = None
    '''

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client

        setup_db(self.app)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
        db_drop_and_create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_add_actor(self):
        res = self.client().post('/actors', json={
            'name': 'Njoud',
            'gender': 'female',
            'age': 25
        }, headers={
            'Authorization': casting_director_token
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # print(data)

    def test_add_movie(self):
        res = self.client().post('/movies', json={
            'title': 'Friends',
            'release_date': '2023-01-01'
        }, headers={
            'Authorization': executive_producer_token
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # print(data)

    def test_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # print(data)

    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # print(data)

    def test_modify_actor(self):
        new_actor = Actor(
            name="Njoud",
            gender="female",
            age=25
        )
        new_actor.insert()
        res = self.client().patch(f'/actors/{new_actor.id}', json={
            'age': 31
        }, headers={
            'Authorization': executive_producer_token
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # print(data)

    def test_modify_movie(self):
        new_movie = Movie(
            title="Friends",
            release_date=datetime.strptime("2023-01-01", '%Y-%m-%d')
        )
        new_movie.insert()
        res = self.client().patch(f'/movies/{new_movie.id}', json={
            'release_date': '2027-03-03'
        }, headers={
            'Authorization': executive_producer_token
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # print(data)

    def test_delete_actor(self):
        new_actor = Actor(
            name="Njoud",
            gender="female",
            age=25
        )
        new_actor.insert()
        res = self.client().delete(f'/actors/{new_actor.id}', headers={
            'Authorization': executive_producer_token
        })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # print(data)

    def test_delete_movie(self):
        new_movie = Movie(
            title="Friends",
            release_date=datetime.strptime("2023-01-01", '%Y-%m-%d')
        )
        new_movie.insert()
        res = self.client().delete(f'/movies/{new_movie.id}', headers={
            'Authorization': executive_producer_token
        })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # print(data)

    def test_add_actor_invalid(self):
        # missing a value (actor name)
        res = self.client().post('/actors', json={
            'gender': 'female',
            'age': 25
        }, headers={
            'Authorization': casting_director_token
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        # print(data)

    def test_add_movie_invalid(self):
        # missing a value (movie title)
        res = self.client().post('/movies', json={
            'release_date': '2023-01-01'
        }, headers={
            'Authorization': executive_producer_token
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        # print(data)

    def test_modify_actor_invalid(self):
        # non-existing actor ID
        res = self.client().patch('/actors/104', json={
            'age': 31
        }, headers={
            'Authorization': executive_producer_token
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        # print(data)

    def test_modify_movie_invalid(self):
        # non-existing Movie ID
        res = self.client().patch('/movies/333', json={
            'release_date': '2027-03-03'
        }, headers={
            'Authorization': executive_producer_token
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        # print(data)

    def test_delete_actor_invalid(self):
        # non-existing actor ID
        res = self.client().delete('/actors/182', headers={
            'Authorization': executive_producer_token
        })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        # print(data)

    def test_delete_movie_invalid(self):
        # non-existing Movie ID
        res = self.client().delete('/movies/222', headers={
            'Authorization': executive_producer_token
        })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        # print(data)

    def test_add_actor_unauthorized_to_public(self):
        # missing authorization header
        res = self.client().post('/actors', json={
            'name': 'Njoud',
            'gender': 'female',
            'age': 25
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        # print(data)

    def test_add_movie_unauthorized_to_director(self):
        # unauthorized director
        res = self.client().post('/movies', json={
            'title': 'Friends',
            'release_date': '2023-01-01'
        }, headers={
            'Authorization': casting_director_token
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        # print(data)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
