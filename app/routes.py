from flask import render_template, jsonify, request, flash, redirect, url_for
from app import app
import json
import os

def load_json_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path) as f:
        return json.load(f)

def save_json_data(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f)

users = load_json_data('users.json')
content = load_json_data('content.json')

def match_content_to_users(users, content):
    if not users or not content:
        return {}
    matches = {}
    for user in users:
        matched_content = []
        for item in content:
            for interest in user['interests']:
                for tag in item['tags']:
                    if interest['type'] == tag['type'] and interest['threshold'] >= tag['threshold']:
                        matched_content.append(item)
                        break
        matches[user['name']] = matched_content
    return matches

@app.route('/')
def index():
    query = request.args.get('q', '')
    page = request.args.get('page', 1, type=int)
    per_page = 2
    filtered_content = [item for item in content if query.lower() in item['title'].lower()]
    paginated_users = users[(page - 1) * per_page:page * per_page]
    matches = match_content_to_users(paginated_users, filtered_content)
    total_pages = (len(users) + per_page - 1) // per_page
    return render_template('index.html', matches=matches, page=page, total_pages=total_pages, query=query)

@app.route('/api/matches', methods=['GET'])
def api_matches():
    matches = match_content_to_users(users, content)
    return jsonify(matches)

@app.route('/upload', methods=['POST'])
def upload_files():
    users_file = request.files.get('users')
    content_file = request.files.get('content')
    if users_file:
        users = json.load(users_file)
        save_json_data('users.json', users)
    if content_file:
        content = json.load(content_file)
        save_json_data('content.json', content)
    flash('Files uploaded successfully!')
    return redirect(url_for('index'))
