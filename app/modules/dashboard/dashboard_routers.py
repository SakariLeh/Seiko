from flask import Blueprint, render_template, request, redirect, url_for

from .dashboard_config import dashboardConf

from app.types import ERoleUser, EMethod

from app.middlewares import role_required_middleware

dashboard_bp = Blueprint("dashboard", __name__)

# @dashboard_bp.route(
#     dashboardConf.r.get_path
# )