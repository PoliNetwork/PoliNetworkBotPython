# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-2019 Dan Tès <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from ..rpc_error import RPCError


class BadRequest(RPCError):
    """Bad Request"""
    CODE = 400
    """``int``: RPC Error Code"""
    NAME = __doc__


class FirstnameInvalid(BadRequest):
    """The first name is invalid"""
    ID = "FIRSTNAME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class LastnameInvalid(BadRequest):
    """The last name is invalid"""
    ID = "LASTNAME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhoneNumberInvalid(BadRequest):
    """The phone number is invalid"""
    ID = "PHONE_NUMBER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhoneCodeHashEmpty(BadRequest):
    """phone_code_hash is missing"""
    ID = "PHONE_CODE_HASH_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhoneCodeEmpty(BadRequest):
    """phone_code is missing"""
    ID = "PHONE_CODE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhoneCodeExpired(BadRequest):
    """The confirmation code has expired"""
    ID = "PHONE_CODE_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhoneCodeInvalid(BadRequest):
    """The confirmation code is invalid"""
    ID = "PHONE_CODE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ApiIdInvalid(BadRequest):
    """The api_id/api_hash combination is invalid"""
    ID = "API_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhoneNumberOccupied(BadRequest):
    """The phone number is already in use"""
    ID = "PHONE_NUMBER_OCCUPIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhoneNumberUnoccupied(BadRequest):
    """The phone number is not yet being used"""
    ID = "PHONE_NUMBER_UNOCCUPIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UsersTooFew(BadRequest):
    """Not enough users (to create a chat, for example)"""
    ID = "USERS_TOO_FEW"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UsersTooMuch(BadRequest):
    """The maximum number of users has been exceeded (to create a chat, for example)"""
    ID = "USERS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class TypeConstructorInvalid(BadRequest):
    """The type constructor is invalid"""
    ID = "TYPE_CONSTRUCTOR_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FilePartInvalid(BadRequest):
    """The file part number is invalid. The value is not between 0 and 2999"""
    ID = "FILE_PART_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FilePartsInvalid(BadRequest):
    """Invalid number of parts. The value is not between 1 and 3000"""
    ID = "FILE_PARTS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FilePartMissing(BadRequest):
    """Part {x} of the file is missing from storage"""
    ID = "FILE_PART_X_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class Md5ChecksumInvalid(BadRequest):
    """The file's checksum did not match the md5_checksum parameter"""
    ID = "MD5_CHECKSUM_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhotoInvalidDimensions(BadRequest):
    """The photo dimensions are invalid"""
    ID = "PHOTO_INVALID_DIMENSIONS"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FieldNameInvalid(BadRequest):
    """The field with the name FIELD_NAME is invalid"""
    ID = "FIELD_NAME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FieldNameEmpty(BadRequest):
    """The field with the name FIELD_NAME is missing"""
    ID = "FIELD_NAME_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MsgWaitFailed(BadRequest):
    """A waiting call returned an error"""
    ID = "MSG_WAIT_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PeerIdInvalid(BadRequest):
    """The id/access_hash combination is invalid"""
    ID = "PEER_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MessageEmpty(BadRequest):
    """The message sent is empty"""
    ID = "MESSAGE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EncryptedMessageInvalid(BadRequest):
    """The special binding message (bind_auth_key_inner) contains invalid data"""
    ID = "ENCRYPTED_MESSAGE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InputMethodInvalid(BadRequest):
    """The method called is invalid"""
    ID = "INPUT_METHOD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PasswordHashInvalid(BadRequest):
    """Two-step verification password is invalid"""
    ID = "PASSWORD_HASH_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UsernameNotOccupied(BadRequest):
    """The username is not occupied by anyone"""
    ID = "USERNAME_NOT_OCCUPIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UsernameInvalid(BadRequest):
    """The username is invalid"""
    ID = "USERNAME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MessageIdInvalid(BadRequest):
    """The message id is invalid"""
    ID = "MESSAGE_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MessageNotModified(BadRequest):
    """The message was not modified"""
    ID = "MESSAGE_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EntityMentionUserInvalid(BadRequest):
    """The mentioned entity is not an user"""
    ID = "ENTITY_MENTION_USER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MessageTooLong(BadRequest):
    """The message text is over 4096 characters"""
    ID = "MESSAGE_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AccessTokenExpired(BadRequest):
    """The bot token is invalid"""
    ID = "ACCESS_TOKEN_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BotMethodInvalid(BadRequest):
    """The method can't be used by bots"""
    ID = "BOT_METHOD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class QueryTooShort(BadRequest):
    """The query is too short"""
    ID = "QUERY_TOO_SHORT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class SearchQueryEmpty(BadRequest):
    """The query is empty"""
    ID = "SEARCH_QUERY_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatIdInvalid(BadRequest):
    """The chat id is invalid"""
    ID = "CHAT_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class DateEmpty(BadRequest):
    """The date argument is empty"""
    ID = "DATE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PersistentTimestampEmpty(BadRequest):
    """The pts is empty"""
    ID = "PERSISTENT_TIMESTAMP_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class CdnMethodInvalid(BadRequest):
    """The method can't be used on CDN DCs"""
    ID = "CDN_METHOD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class VolumeLocNotFound(BadRequest):
    """The volume location can't be found"""
    ID = "VOLUME_LOC_NOT_FOUND"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FileIdInvalid(BadRequest):
    """The file id is invalid"""
    ID = "FILE_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class LocationInvalid(BadRequest):
    """The file address is invalid"""
    ID = "LOCATION_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatAdminRequired(BadRequest):
    """The method requires chat admin privileges"""
    ID = "CHAT_ADMIN_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhoneNumberBanned(BadRequest):
    """The phone number is banned"""
    ID = "PHONE_NUMBER_BANNED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AboutTooLong(BadRequest):
    """The about text is too long"""
    ID = "ABOUT_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MultiMediaTooLong(BadRequest):
    """The album contains more than 10 items"""
    ID = "MULTI_MEDIA_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UsernameOccupied(BadRequest):
    """The username is already in use"""
    ID = "USERNAME_OCCUPIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BotInlineDisabled(BadRequest):
    """The inline feature of the bot is disabled"""
    ID = "BOT_INLINE_DISABLED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InlineResultExpired(BadRequest):
    """The inline bot query expired"""
    ID = "INLINE_RESULT_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InviteHashInvalid(BadRequest):
    """The invite link hash is invalid"""
    ID = "INVITE_HASH_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserAlreadyParticipant(BadRequest):
    """The user is already a participant of this chat"""
    ID = "USER_ALREADY_PARTICIPANT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class TtlMediaInvalid(BadRequest):
    """The media does not support self-destruction"""
    ID = "TTL_MEDIA_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MaxIdInvalid(BadRequest):
    """The max_id parameter is invalid"""
    ID = "MAX_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChannelInvalid(BadRequest):
    """The channel parameter is invalid"""
    ID = "CHANNEL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class DcIdInvalid(BadRequest):
    """The dc_id parameter is invalid"""
    ID = "DC_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class LimitInvalid(BadRequest):
    """The limit parameter is invalid"""
    ID = "LIMIT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class OffsetInvalid(BadRequest):
    """The offset parameter is invalid"""
    ID = "OFFSET_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EmailInvalid(BadRequest):
    """The email provided is invalid"""
    ID = "EMAIL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserIsBot(BadRequest):
    """A bot cannot send messages to other bots or to itself"""
    ID = "USER_IS_BOT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class WebpageCurlFailed(BadRequest):
    """Telegram server could not fetch the provided URL"""
    ID = "WEBPAGE_CURL_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StickersetInvalid(BadRequest):
    """The requested sticker set is invalid"""
    ID = "STICKERSET_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PeerFlood(BadRequest):
    """The method can't be used because your account is limited"""
    ID = "PEER_FLOOD"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MediaCaptionTooLong(BadRequest):
    """The media caption is longer than 1024 characters"""
    ID = "MEDIA_CAPTION_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserNotMutualContact(BadRequest):
    """The user is not a mutual contact"""
    ID = "USER_NOT_MUTUAL_CONTACT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserChannelsTooMuch(BadRequest):
    """The user is already in too many channels or supergroups"""
    ID = "USER_CHANNELS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ApiIdPublishedFlood(BadRequest):
    """You are using an API key that is limited on the server side"""
    ID = "API_ID_PUBLISHED_FLOOD"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserNotParticipant(BadRequest):
    """The user is not a member of this chat"""
    ID = "USER_NOT_PARTICIPANT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChannelPrivate(BadRequest):
    """The channel/supergroup is not accessible"""
    ID = "CHANNEL_PRIVATE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MessageIdsEmpty(BadRequest):
    """The requested message doesn't exist"""
    ID = "MESSAGE_IDS_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class WebpageMediaEmpty(BadRequest):
    """The URL doesn't contain any valid media"""
    ID = "WEBPAGE_MEDIA_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class QueryIdInvalid(BadRequest):
    """The callback query id is invalid"""
    ID = "QUERY_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MediaEmpty(BadRequest):
    """The media is invalid"""
    ID = "MEDIA_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserIsBlocked(BadRequest):
    """The user blocked you"""
    ID = "USER_IS_BLOCKED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class YouBlockedUser(BadRequest):
    """You blocked this user"""
    ID = "YOU_BLOCKED_USER"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AdminsTooMuch(BadRequest):
    """The chat has too many administrators"""
    ID = "ADMINS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BotsTooMuch(BadRequest):
    """The chat has too many bots"""
    ID = "BOTS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserAdminInvalid(BadRequest):
    """The action requires admin privileges"""
    ID = "USER_ADMIN_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InputUserDeactivated(BadRequest):
    """The target user has been deactivated"""
    ID = "INPUT_USER_DEACTIVATED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PasswordRecoveryNa(BadRequest):
    """The password recovery e-mail is not available"""
    ID = "PASSWORD_RECOVERY_NA"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PasswordEmpty(BadRequest):
    """The password entered is empty"""
    ID = "PASSWORD_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhoneNumberFlood(BadRequest):
    """This number has tried to login too many times"""
    ID = "PHONE_NUMBER_FLOOD"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class TakeoutInvalid(BadRequest):
    """The takeout id is invalid"""
    ID = "TAKEOUT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class TakeoutRequired(BadRequest):
    """The method must be invoked inside a takeout session"""
    ID = "TAKEOUT_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MessagePollClosed(BadRequest):
    """You can't interact with a closed poll"""
    ID = "MESSAGE_POLL_CLOSED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MediaInvalid(BadRequest):
    """The media is invalid"""
    ID = "MEDIA_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BotScoreNotModified(BadRequest):
    """The bot score was not modified"""
    ID = "BOT_SCORE_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserBotRequired(BadRequest):
    """The method can be used by bots only"""
    ID = "USER_BOT_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ImageProcessFailed(BadRequest):
    """The server failed to process your image"""
    ID = "IMAGE_PROCESS_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UsernameNotModified(BadRequest):
    """The username was not modified"""
    ID = "USERNAME_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class CallAlreadyAccepted(BadRequest):
    """The call is already accepted"""
    ID = "CALL_ALREADY_ACCEPTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class CallAlreadyDeclined(BadRequest):
    """The call is already declined"""
    ID = "CALL_ALREADY_DECLINED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhotoExtInvalid(BadRequest):
    """The photo extension is invalid"""
    ID = "PHOTO_EXT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ExternalUrlInvalid(BadRequest):
    """The external media URL is invalid"""
    ID = "EXTERNAL_URL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatNotModified(BadRequest):
    """The chat settings were not modified"""
    ID = "CHAT_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ResultsTooMuch(BadRequest):
    """The result contains too many items"""
    ID = "RESULTS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ResultIdDuplicate(BadRequest):
    """The result contains items with duplicated identifiers"""
    ID = "RESULT_ID_DUPLICATE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AccessTokenInvalid(BadRequest):
    """The bot access token is invalid"""
    ID = "ACCESS_TOKEN_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InviteHashExpired(BadRequest):
    """The chat invite link is no longer valid"""
    ID = "INVITE_HASH_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserBannedInChannel(BadRequest):
    """You are limited, check @SpamBot for details"""
    ID = "USER_BANNED_IN_CHANNEL"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MessageEditTimeExpired(BadRequest):
    """You can no longer edit this message"""
    ID = "MESSAGE_EDIT_TIME_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FolderIdInvalid(BadRequest):
    """The folder id is invalid"""
    ID = "FOLDER_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MegagroupPrehistoryHidden(BadRequest):
    """The action failed because the supergroup has the pre-history hidden"""
    ID = "MEGAGROUP_PREHISTORY_HIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatLinkExists(BadRequest):
    """The action failed because the supergroup is linked to a channel"""
    ID = "CHAT_LINK_EXISTS"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class LinkNotModified(BadRequest):
    """The chat link was not modified because you tried to link to the same target"""
    ID = "LINK_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BroadcastIdInvalid(BadRequest):
    """The channel is invalid"""
    ID = "BROADCAST_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MegagroupIdInvalid(BadRequest):
    """The supergroup is invalid"""
    ID = "MEGAGROUP_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ButtonDataInvalid(BadRequest):
    """The button callback data contains invalid data or exceeds 64 bytes"""
    ID = "BUTTON_DATA_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StartParamInvalid(BadRequest):
    """The start parameter is invalid"""
    ID = "START_PARAM_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ArticleTitleEmpty(BadRequest):
    """The article title is empty"""
    ID = "ARTICLE_TITLE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FilePartTooBig(BadRequest):
    """The size limit (512 KB) for the content of the file part has been exceeded"""
    ID = "FILE_PART_TOO_BIG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FilePartEmpty(BadRequest):
    """The file part sent is empty"""
    ID = "FILE_PART_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FilePartSizeInvalid(BadRequest):
    """512 KB cannot be evenly divided by part_size"""
    ID = "FILE_PART_SIZE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FilePartSizeChanged(BadRequest):
    """The part size is different from the size of one of the previous parts in the same file"""
    ID = "FILE_PART_SIZE_CHANGED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FileMigrate(BadRequest):
    """The file is in Data Center No. {x}"""
    ID = "FILE_MIGRATE_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ResultTypeInvalid(BadRequest):
    """The result type is invalid"""
    ID = "RESULT_TYPE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhotoThumbUrlEmpty(BadRequest):
    """The photo thumb URL is empty"""
    ID = "PHOTO_THUMB_URL_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhotoThumbUrlInvalid(BadRequest):
    """The photo thumb URL is invalid"""
    ID = "PHOTO_THUMB_URL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhotoContentUrlEmpty(BadRequest):
    """The photo content URL is empty"""
    ID = "PHOTO_CONTENT_URL_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhotoContentTypeInvalid(BadRequest):
    """The photo content type is invalid"""
    ID = "PHOTO_CONTENT_TYPE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class WebdocumentInvalid(BadRequest):
    """The web document is invalid"""
    ID = "WEBDOCUMENT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class WebdocumentUrlEmpty(BadRequest):
    """The web document URL is empty"""
    ID = "WEBDOCUMENT_URL_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class WebdocumentUrlInvalid(BadRequest):
    """The web document URL is invalid"""
    ID = "WEBDOCUMENT_URL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class WebdocumentMimeInvalid(BadRequest):
    """The web document mime type is invalid"""
    ID = "WEBDOCUMENT_MIME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ButtonUrlInvalid(BadRequest):
    """The button url is invalid"""
    ID = "BUTTON_URL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AuthBytesInvalid(BadRequest):
    """The authorization bytes are invalid"""
    ID = "AUTH_BYTES_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChannelsTooMuch(BadRequest):
    """You have joined too many channels or supergroups"""
    ID = "CHANNELS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AdminRankInvalid(BadRequest):
    """The custom administrator title is invalid or is longer than 16 characters"""
    ID = "ADMIN_RANK_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AdminRankEmojiNotAllowed(BadRequest):
    """Emojis are not allowed in custom administrator titles"""
    ID = "ADMIN_RANK_EMOJI_NOT_ALLOWED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FileReferenceEmpty(BadRequest):
    """The file reference is empty"""
    ID = "FILE_REFERENCE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FileReferenceInvalid(BadRequest):
    """The file reference is invalid"""
    ID = "FILE_REFERENCE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


