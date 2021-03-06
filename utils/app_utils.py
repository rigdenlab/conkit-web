import components
from dash.dash import no_update
import layouts
from utils import UrlIndex, postgres_utils, cache_utils
from utils import decompress_data, compress_data
from utils.exceptions import IntegrityError, UserExists, EmailAlreadyUsed


def recover_account(username, email, secret, password_1, password_2, logger):

    if password_1 != password_2:
        return components.InvalidPasswordRecoverAccount()

    success = postgres_utils.recover_account(username, email, secret, password_1)

    if success:
        logger.info('Username {} reset password successful'.format(username))
        return components.SuccessRecoverAccount()

    logger.info('Username {} failed to reset password'.format(username))
    return components.FailureRecoverAccount()


def change_password(new_password, old_password, cache, session_id, logger):
    username = decompress_data(cache.hget(session_id, cache_utils.CacheKeys.USER.value))
    if postgres_utils.change_password(username, old_password, new_password):
        logger.info('Session {} user {} changed password'.format(session_id, username))
        return components.SuccessChangePasswordAlert(username)
    else:
        return components.FailChangePasswordAlert(username)


def create_user(username, password, email, session_id, cache, logger):
    if any([True for x in (username, password, email) if x is None or x == '']):
        return True, None, no_update, no_update, no_update, no_update
    try:
        postgres_utils.create_user(username, password, email)
        logger.info('Session {} created user {} - {}'.format(session_id, username, email))
        cache.hset(session_id, cache_utils.CacheKeys.USER.value, compress_data(username))
        return False, components.SuccessCreateUserModal(username), None, None, None, no_update
    except (UserExists, EmailAlreadyUsed, IntegrityError) as e:
        return True, None, no_update, no_update, no_update, no_update


def user_logout(session_id, cache, logger):
    cache_utils.clear_cache(session_id, cache)
    cache.hdel(session_id, cache_utils.CacheKeys.USER.value)
    cache.hdel(session_id, cache_utils.CacheKeys.SESSION_PKID.value)
    logger.info('Session {} logout user'.format(session_id))
    return no_update, components.SuccessLogoutAlert(), components.UserPortalCardBody(None)


def user_login(username, password, session_id, cache, logger):
    if postgres_utils.userlogin(username, password):
        logger.info('Session {} login user {}'.format(session_id, username))
        cache.hset(session_id, cache_utils.CacheKeys.USER.value, compress_data(username))
        return False, components.SuccessLoginAlert(username), components.UserPortalCardBody(username)
    else:
        return True, None, no_update


def serve_url(url, session_id, cache, logger):
    if cache.hexists(session_id, cache_utils.CacheKeys.USER.value):
        username = decompress_data(cache.hget(session_id, cache_utils.CacheKeys.USER.value))
    else:
        username = None

    if url == UrlIndex.HOME.value or url == UrlIndex.ROOT.value:
        return layouts.Home(session_id, username)
    elif url == UrlIndex.CONTACT.value:
        return layouts.Contact(session_id, username)
    elif url == UrlIndex.PLOT.value:
        if cache.hexists(session_id, cache_utils.CacheKeys.FIGURE_JSON.value):
            figure = decompress_data(cache.hget(session_id, cache_utils.CacheKeys.FIGURE_JSON.value))
            display_settings = decompress_data(cache.hget(session_id, cache_utils.CacheKeys.DISPLAY_CONTROL_JSON.value))
            return layouts.Plot(session_id, username, figure, display_settings)
        else:
            return layouts.Plot(session_id, username)
    elif url == UrlIndex.HELP.value:
        return layouts.Help(session_id, username, cache)
    elif url == UrlIndex.RIGDEN.value:
        return layouts.RigdenLab(session_id, username)
    elif url == UrlIndex.PRIVACY_POLICY.value:
        return layouts.PrivacyPolicy(session_id)
    elif url in (UrlIndex.USERS_PORTAL.value, UrlIndex.CREATE_USER.value, UrlIndex.CHANGE_PASSWORD.value,
                 UrlIndex.SHARE_SESSIONS.value, UrlIndex.USER_STORAGE.value, UrlIndex.ACCOUNT_RECOVERY.value):
        if not postgres_utils.is_postgres_available(logger):
            return layouts.PostgresConnectionError()
        elif url == UrlIndex.USERS_PORTAL.value:
            return layouts.UsersPortal(username)
        elif url == UrlIndex.CREATE_USER.value:
            return layouts.CreateUser(username)
        elif url == UrlIndex.CHANGE_PASSWORD.value:
            return layouts.ChangeUserPassword(username)
        elif url == UrlIndex.SHARE_SESSIONS.value:
            return layouts.ShareSession(username)
        elif url == UrlIndex.ACCOUNT_RECOVERY.value:
            return layouts.AccountRecoveryPortal()
        elif url == UrlIndex.USER_STORAGE.value:
            if cache.hexists(session_id, cache_utils.CacheKeys.SESSION_PKID.value):
                session_pkid = int(cache.hget(session_id, cache_utils.CacheKeys.SESSION_PKID.value))
                return layouts.UserStorage(username, session_pkid)
            else:
                return layouts.UserStorage(username)
    else:
        logger.error('404 page not found {}'.format(url))
        return layouts.noPage(url, username)
