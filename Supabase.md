# Create a new user
By default, the user needs to verify their email address before logging in. To turn this off, disable Confirm email in your project.
Confirm email determines if users need to confirm their email address after signing up.
If Confirm email is enabled, a user is returned but session is null.
If Confirm email is disabled, both a user and a session are returned.
By default, when the user confirms their email address, they are redirected to the SITE_URL. You can modify your SITE_URL or add additional redirect URLs in your project.
If sign_up() is called for an existing confirmed user:
When both Confirm email and Confirm phone (even when phone provider is disabled) are enabled in your project, an obfuscated/fake user object is returned.
When either Confirm email or Confirm phone (even when phone provider is disabled) is disabled, the error message, User already registered is returned.
To fetch the currently logged-in user, refer to get_user().

response = supabase.auth.sign_up(
    {"email": "email@example.com", "password": "password"}
)

{
  "user": {
    "id": "11111111-1111-1111-1111-111111111111",
    "app_metadata": {
      "provider": "email",
      "providers": [
        "email"
      ]
    },
    "user_metadata": {},
    "aud": "authenticated",
    "confirmation_sent_at": null,
    "recovery_sent_at": null,
    "email_change_sent_at": null,
    "new_email": null,
    "invited_at": null,
    "action_link": null,
    "email": "email@example.com",
    "phone": "",
    "created_at": "2024-06-17T00:19:25.760110Z",
    "confirmed_at": null,
    "email_confirmed_at": "2024-06-17T00:19:25.779181Z",
    "phone_confirmed_at": null,
    "last_sign_in_at": "2024-06-17T00:19:25.785489Z",
    "role": "authenticated",
    "updated_at": "2024-06-17T00:19:25.794650Z",
    "identities": [
      {
        "id": "11111111-1111-1111-1111-111111111111",
        "user_id": "11111111-1111-1111-1111-111111111111",
        "identity_data": {
          "email": "email@example.com",
          "sub": "11111111-1111-1111-1111-111111111111"
        },
        "provider": "email",
        "created_at": "2024-06-17T00:19:25.774522Z",
        "last_sign_in_at": "2024-06-17T00:19:25.774498Z",
        "updated_at": "2024-06-17T00:19:25.774522Z"
      }
    ],
    "factors": null
  },
  "session": {
    "provider_token": null,
    "provider_refresh_token": null,
    "access_token": "<ACCESS_TOKEN>",
    "refresh_token": "<REFRESH_TOKEN>",
    "expires_in": 3600,
    "expires_at": 1700000000,
    "token_type": "bearer",
    "user": {
      "id": "11111111-1111-1111-1111-111111111111",
      "app_metadata": {
        "provider": "email",
        "providers": [
          "email"
        ]
      },
      "user_metadata": {},
      "aud": "authenticated",
      "confirmation_sent_at": null,
      "recovery_sent_at": null,
      "email_change_sent_at": null,
      "new_email": null,
      "invited_at": null,
      "action_link": null,
      "email": "email@example.com",
      "phone": "",
      "created_at": "2024-06-17T00:19:25.760110Z",
      "confirmed_at": null,
      "email_confirmed_at": "2024-06-17T00:19:25.779181Z",
      "phone_confirmed_at": null,
      "last_sign_in_at": "2024-06-17T00:19:25.785489Z",
      "role": "authenticated",
      "updated_at": "2024-06-17T00:19:25.794650Z",
      "identities": [
        {
          "id": "11111111-1111-1111-1111-111111111111",
          "user_id": "11111111-1111-1111-1111-111111111111",
          "identity_data": {
            "email": "email@example.com",
            "sub": "11111111-1111-1111-1111-111111111111"
          },
          "provider": "email",
          "created_at": "2024-06-17T00:19:25.774522Z",
          "last_sign_in_at": "2024-06-17T00:19:25.774498Z",
          "updated_at": "2024-06-17T00:19:25.774522Z"
        }
      ],
      "factors": null
    }
  }
}
