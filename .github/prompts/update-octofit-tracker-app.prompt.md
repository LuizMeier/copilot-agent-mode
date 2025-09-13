mode: 'agent'
model: GPT-4.1

description: |
  Atualizações para o app Django Octofit Tracker.

# Django App Updates

- Todos os arquivos do projeto Django estão em `octofit-tracker/backend/octofit_tracker`.

1. Atualize `settings.py` para conexão com MongoDB e CORS.
2. Atualize `models.py`, `serializers.py`, `urls.py`, `views.py`, `tests.py` e `admin.py` para suportar as coleções users, teams, activities, leaderboard e workouts.
3. Garanta que `/` aponte para a API e que `api_root` esteja presente em `urls.py`.
