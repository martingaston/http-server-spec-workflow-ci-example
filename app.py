from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    make_response,
    send_file,
)
import json

app = Flask(__name__)


@app.route("/simple_get", methods=["GET"])
def simple_get():
    return ""


@app.route("/simple_get_with_body", methods=["GET"])
def simple_get_with_body():
    return "Hello world"


@app.route("/head_request", methods=["HEAD"])
def head_does_not_include_body():
    return ""


@app.route("/method_options", methods=["GET"])
def finding_options_for_endpoint_with_only_get():
    return ""


@app.route("/method_options2", methods=["GET", "PUT", "POST"])
def finding_options_for_endpoint_with_multiple_verbs():
    return ""


@app.route("/echo_body", methods=["POST"])
def posting_echoes_the_body():
    return request.get_data()


@app.route("/redirect", methods=["GET"])
def get_a_resource_moved_to_a_different_location():
    return redirect(url_for("posting_echoes_the_body"), 301)


@app.route("/text_response", methods=["GET"])
def get_request_to_text_response():
    text = "text response"
    resp = make_response(text, 200)
    resp.headers["Content-Type"] = "text/plain;charset=utf-8"
    return resp


@app.route("/html_response", methods=["GET"])
def get_request_to_html_response():
    html = "<html><body><p>HTML Response</p></body></html>"
    resp = make_response(html, 200)
    resp.headers["Content-Type"] = "text/html;charset=utf-8"
    return resp


@app.route("/json_response", methods=["GET"])
def get_request_to_json_response():
    json_resp = json.dumps({"key1": "value1", "key2": "value2"}, separators=(",", ":"))
    resp = make_response(json_resp, 200)
    resp.headers["Content-Type"] = "application/json;charset=utf-8"
    return resp


@app.route("/xml_response", methods=["GET"])
def get_request_to_xml_response():
    xml = "<note><body>XML Response</body></note>"
    resp = make_response(xml, 200)
    resp.headers["Content-Type"] = "application/xml;charset=utf-8"
    return resp


@app.route("/health-check.html", methods=["GET"])
def get_healthcheck():
    resp = make_response(render_template("health-check.html"), 200)
    resp.headers["Content-Type"] = "text/html;charset=utf-8"
    return resp


@app.route("/kitteh.jpg", methods=["GET"])
def get_kitteh():
    return send_file("static/kitteh.jpg")


@app.route("/doggo.png", methods=["GET"])
def get_doggo():
    return send_file("static/doggo.png")


@app.route("/kisses.gif", methods=["GET"])
def get_kisses():
    return send_file("static/kisses.gif")


@app.errorhandler(405)
def method_not_allowed(error):
    resp = make_response("", 405)
    resp.headers["Allow"] = ", ".join(error.valid_methods)
    return resp
