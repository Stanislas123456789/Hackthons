# LLaMA Chatbot

A beautiful chatbot interface powered by Cerebras LLaMA model.

## Features

- Attractive, modern chat interface
- Distinct message bubbles for user and bot
- Enter key support for sending messages
- Smooth animations for new messages
- Responsive design

## Deployment Instructions

### Option 1: Manual Deployment

#### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 2. Set Environment Variables

For security, it's recommended to set your Cerebras API key as an environment variable:

**On Windows (Command Prompt):**
```cmd
set CEREBRAS_API_KEY=your_api_key_here
```

**On Windows (PowerShell):**
```powershell
$env:CEREBRAS_API_KEY="your_api_key_here"
```

**On Linux/macOS:**
```bash
export CEREBRAS_API_KEY=your_api_key_here
```

Alternatively, you can modify the app.py file to directly set your API key, though this is less secure:

```python
api_key = "your_api_key_here"  # instead of os.environ.get("CEREBRAS_API_KEY", "fallback_key")
```

#### 3. Run the Application

```bash
python app.py
```

### Option 2: Automated Deployment

You can also use the provided deployment script which will automatically install dependencies, prompt for your API key, and start the application:

```bash
python deploy.py
```

When prompted, enter your Cerebras API key or press Enter to use the fallback key (less secure).

### 4. Access the Application

Once running, the application will be accessible at:
- Local access: http://localhost:5000
- Network access: http://your_machine_ip:5000

To find your machine's IP address:

**On Windows:**
```cmd
ipconfig
```

**On Linux/macOS:**
```bash
ifconfig
```

Look for the IPv4 address in the output.

## Usage

1. Open your browser and navigate to http://localhost:5000 (or your machine's IP address if accessing from another device)
2. Type your message in the input field at the bottom
3. Press Enter or click "Envoyer" to send your message
4. The bot's response will appear in the chat window

## Security Note

For production deployment, always use environment variables for API keys rather than hardcoding them in the source code.
