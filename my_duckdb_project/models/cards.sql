with source as (
    select * from {{ source('raw', 'cards') }}
),

renamed_and_casted as (
    select
        -- Identifiers
        cast("User" as integer) as user_id,
        cast("CARD INDEX" as integer) as card_index,
        
        -- Card Details
        "Card Brand" as card_brand,
        case 
            when "Card Type" = 'Debit (Prepaid)' then 'Prepaid'
            else "Card Type"
        end as card_type,
        "Card Number" as card_number,
        "Expires" as expires,
        -- CVV: Remove leading zeros by casting to int and back to string
        ltrim("CVV", '0') as cvv,
        "Has Chip" as has_chip,
        cast("Cards Issued" as integer) as cards_issued,
        
        -- Financials: Remove '$' and cast to integer
        cast(replace("Credit Limit", '$', '') as integer) as credit_limit,
        
        -- Dates & Security
        "Acct Open Date" as acct_open_date,
        cast("Year PIN last Changed" as integer) as year_pin_last_changed,
        "Card on Dark Web" as card_on_dark_web
        
    from source
)

select * from renamed_and_casted