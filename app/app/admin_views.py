from app import app 

@app.route("/admin/dashboard")
def dashboard():
    return "Admin dashboard"

@app.route("/admin/profile")   
def profile():
      return "Admin Profile"