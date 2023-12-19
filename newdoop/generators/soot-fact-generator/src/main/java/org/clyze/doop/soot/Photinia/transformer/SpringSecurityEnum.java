package org.clyze.doop.soot.Photinia.transformer;

public enum SpringSecurityEnum implements EnumMessage {
    WEB_ASYNC_FILTER("org.springframework.security.web.context.request.async.WebAsyncManagerIntegrationFilter"),
    SECURITY_CONTEXT_FILTER("org.springframework.security.web.context.SecurityContextPersistenceFilter"), // Default
    HEADERS_FILTER("org.springframework.security.web.header.HeaderWriterFilter"), // Default
    CSRF_FILTER("org.springframework.security.web.csrf.CsrfFilter"), // Default
    LOGOUT_FILTER("org.springframework.security.web.authentication.logout.LogoutFilter"), // Default
    FORM_LOGIN_FILTER("org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter"), // Default
    REQUEST_CACHE_FILTER("org.springframework.security.web.savedrequest.RequestCacheAwareFilter"),
    SERVLET_API_SUPPORT_FILTER("org.springframework.security.web.servletapi.SecurityContextHolderAwareRequestFilter"),
    REMEMBER_ME_FILTER("org.springframework.security.web.authentication.rememberme.RememberMeAuthenticationFilter"),
    ANONYMOUS_FILTER("org.springframework.security.web.authentication.AnonymousAuthenticationFilter"), // Default
    SESSION_MANAGEMENT_FILTER("org.springframework.security.web.session.SessionManagementFilter"), // Default
    EXCEPTION_TRANSLATION_FILTER("org.springframework.security.web.access.ExceptionTranslationFilter"), // Default
    FILTER_SECURITY_INTERCEPTOR("org.springframework.security.web.access.intercept.FilterSecurityInterceptor"); // Default



    private String filter;

    SpringSecurityEnum(String filter) {
        this.filter = filter;
    }

    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }


    @Override
    public Object getValue() {
        return filter;
    }
}
