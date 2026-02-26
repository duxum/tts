# tts
The repository is part of assignment. In this section I describe the script and Docker workflows. Other content is described in the write up.

## Script Usage
```
python run.py "Muraho, nagufasha gute uyu munsi?" --output greeting
```

The command will generate audio in the `output/greeting.wav` from current directory.

## Docker Usage
### Build Image
```
docker build -t tts-generator .
```

### Running Container
```
docker run \
  --rm \
  -v $(pwd)/output:/app/output \
  tts-generator \
  "Muraho, nagufasha gute uyu munsi?"
```

Run a container, mounting the local output directory so the generated file persists and becomes accessible on your host.
