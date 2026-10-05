cat > app.py << 'EOF'
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def greet(name):
    message = "Welcome, " + name + ". Have a great day!"
    return message
EOF

