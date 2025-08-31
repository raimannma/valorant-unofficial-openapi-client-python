uvx openapi-python-client generate --url https://beta.api.henrikdev.xyz/openapi.json --output-path . --overwrite --meta uv --config generate-config.yaml
uv sync -U --all-groups

# Add uv.lock to .gitignore
echo "uv.lock" >> .gitignore
