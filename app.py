import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime, date

from database.models import db_drop_and_create_all, setup_db, Movie, Actor
from auth.auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    APP = Flask(__name__)
    setup_db(APP)
    # CORS(app)

    # APP = create_app()

    # if __name__ == '__main__':
    #    APP.run(host='127.0.0.1', port=5000, debug=True)

    db_drop_and_create_all()

    @APP.route('/token')
    def get_token():
        return jsonify({
            'success': True
        }), 200

    @APP.route('/actors', methods=['GET'])
    def get_actors():
        # query all listed actors
        actors = Actor.query.all()
        formatted_actors = [actor.format() for actor in actors]
        # return results with the success code
        return jsonify({
            'success': True,
            'actors': formatted_actors
        }), 200

    @APP.route('/movies', methods=['GET'])
    def get_movies():
        # query all listed actors
        movies = Movie.query.all()
        formatted_movies = [movie.format() for movie in movies]
        # return results with the success code
        return jsonify({
            'success': True,
            'movies': formatted_movies
        }), 200

    @APP.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(payload, id):
        # code
        actor = Actor.query.filter(Actor.id == id).one_or_none()
        if not actor:
            abort(404)
        try:
            actor.delete()
        except BaseException:
            abort(400)

        return jsonify({'success': True, 'delete': id}), 200

    @APP.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(payload, id):
        # code
        movie = Movie.query.filter(Movie.id == id).one_or_none()
        if not movie:
            abort(404)
        try:
            movie.delete()
        except BaseException:
            abort(400)

        return jsonify({'success': True, 'delete': id}), 200

    @APP.route('/actors', methods=['POST'])
    @requires_auth('post:actor')
    def post_actor(payload):
        data = request.get_json()
        try:
            actor = Actor(name=data['name'], gender=data['gender'], age=data['age'])
            actor.insert()

            return jsonify({
                'success': True,
                'actor': actor.format()
            }), 200
        except:
            abort(422)

    @APP.route('/movies', methods=['POST'])
    @requires_auth('post:movie')
    def post_movie(payload):
        data = request.get_json()
        try:
            movie = Movie(title=data['title'], release_date=datetime.strptime(data['release_date'], '%Y-%m-%d'))
            movie.insert()

            return jsonify({
                'success': True,
                'movie': movie.format()
            }), 200
        except:
            abort(422)

    @APP.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def modify_actor(payload, id):
        actor = Actor.query.get(id)
        if actor is None:
            abort(404)

        data = request.get_json()
        if 'name' in data:
            actor.name = data['name']

        if 'gender' in data:
            actor.gender = data['gender']

        if 'age' in data:
            actor.age = data['age']

        try:
            actor.update()
        except BaseException:
            abort(400)

        return jsonify({
            'success': True,
            'actor': actor.format()
        }), 200

    @APP.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def modify_movie(payload, id):
        movie = Movie.query.get(id)
        if movie is None:
            abort(404)

        data = request.get_json()
        if 'title' in data:
            movie.title = data['title']

        if 'release_date' in data:
            movie.release_date = datetime.strptime(data['release_date'], '%Y-%m-%d')

        try:
            movie.update()
        except BaseException:
            abort(400)

        return jsonify({
            'success': True,
            'movie': movie.format()
        }), 200

    # error handling

    @APP.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @APP.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource Not Found"
        }), 404

    '''
    error handler for AuthError
    '''

    @APP.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code

    @APP.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": 'Unauthorized'
        }), 401

    @APP.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": 'Bad Request'
        }), 400

    return APP


app = create_app()

