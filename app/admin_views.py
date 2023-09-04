from app import app

@app.route("/admin/dashboard")
def admin_dashboard():
    return "Admin dashboard"

@app.route("/admin/profile")
def admin_profile():
    return "<h1 style='color: blue' >Admin profile</h1>"