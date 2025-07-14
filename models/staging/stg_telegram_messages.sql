with raw_messages as (

    select
        message_id,
        channel,
        message,
        date,
        media
    from raw.telegram_messages

)

select
    message_id,
    channel,
    message,
    date::date as date_day,
    media
from raw_messages
