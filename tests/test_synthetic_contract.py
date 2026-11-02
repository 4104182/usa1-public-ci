"""Public fake payment/license state machine; never uses real payment data."""
import unittest

def license_issued(event):
    return (event.get("verified") is True and
            event.get("test_only") is True and
            event.get("revoked") is False and
            event.get("payment_kind") == "synthetic")

class SimulatedLicenseContracts(unittest.TestCase):
    def test_unverified_rejected(self):
        self.assertFalse(license_issued({"verified": False, "test_only": True, "revoked": False, "payment_kind": "synthetic"}))
    def test_missing_verification_rejected(self):
        self.assertFalse(license_issued({"test_only": True, "revoked": False, "payment_kind": "synthetic"}))
    def test_non_synthetic_rejected(self):
        self.assertFalse(license_issued({"verified": True, "test_only": True, "revoked": False, "payment_kind": "real"}))
    def test_revoked_rejected(self):
        self.assertFalse(license_issued({"verified": True, "test_only": True, "revoked": True, "payment_kind": "synthetic"}))
    def test_synthetic_allowed(self):
        self.assertTrue(license_issued({"verified": True, "test_only": True, "revoked": False, "payment_kind": "synthetic"}))

if __name__ == "__main__":
    unittest.main()
