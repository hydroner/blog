#_*_ coding:utf-8 _*_

def setupmethod(f):

    def wrapper_func(self, *args, **kwargs):
        if self.debug and self._got_first_request:
            raise AssertionError()
        return f(self, *args, **kwargs)
    return update_wrapper(wrapper_func, f)


class Flask(object):

    def __init__(self):
        self._got_first_request = False

    @property
    def got_first_request(self):
        return self._got_first_request

    def run(self, host=None, port=None, debug=None, **options):
        from werkzeug.serving import run_simple
        if host is None:
            host = '127.0.0.1'
        if port is None:
            server_name = self.config['SERVER_NAME']
            if server_name and ':' in server_name:
                port = int(server_name.rsplit(':', 1)[1])
            else:
                port = 5000
        if debug is not None:
            self.debug = bool(debug)
        options.setdefault('use_reloader', self.debug)
        options.setdefault('use_debugger', self.debug)
        try:
            run_simple(host, port, self, **options)
        finally:
                    self._got_first_request = Fasle

    @setupmethod
    def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
        if endpoint is None:
            endpoint = _endpoint_from_view_func(view_func)
        options['endpoint'] = endpoint
        methods = options.pop('methods', None)
        if methods is None:
            methods = getattr(view_func, 'methods', None) or ('GET',)
        methods = set(methods)
        required_methods = set(getattr(view_func, 'required_methods', ()))
        provide_automatic_options = getattr(view_func,
            'provide_automatic_options', None)
        if provide_automatic_options is None:
            if 'OPTIONS' not in methods:
                provide_automatic_options = True
                required_methods.add('OPTIon
             
    
    def route(self, rule, **options):

        def decorator(f):
            endpoint = options.pop('endpoint', None)
            self.add_url_rule(rule, endpoint, f, **options)
            return f
        return decorator
    
    #生成endpoint-view_func的映射
    @setupmethod
    def endpoint(self, endpoint):
        def decorator(f):
            self.view_functions[endpoint] = f
        return decorator

    def raise_routing_exception(self, request):
        if not self.debug \
            or not isinstance(request.routing_exception, RequestRedirect) \
            or request.method in ('GET', 'HEAD', 'OPTIONS'):
            raise request.routing_exception
        from .debughelpers import FormDataRoutingRedirect
        raise FormDataRoutingRedirect(request)

    def dispatch_request(self):
        req = _request_ctx_stack.top.request
        if req.routing_exception is not None:
            self.raise_routing_exception(req)
        rule = req.url_rule
        if getattr(rule, 'provide_automatic_options',False) \
            and req.method == 'OPTIONS':
            return self.make_default_options_response()
        return self.view_functions[rule.endpoint](**req.view_args)    