Feature: OTP Validation

    Scenario: Validate OTP Expiry

        Given user receives OTP
        When OTP expires
        Then login should fail