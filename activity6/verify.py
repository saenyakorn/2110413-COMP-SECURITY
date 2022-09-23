from OpenSSL import crypto
import pem


def verify(target_filename, intermediate_filenames, root_filename):
    with open(target_filename, 'r') as cert_file:
        cert = cert_file.read()
    int_certs = []
    for filename in intermediate_filenames:
        with open(filename, 'r') as cert_file:
            int_certs.append(cert_file.read())
    pems = pem.parse_file(root_filename)
    trusted_certs = []
    for mypem in pems:
        trusted_certs.append(str(mypem))
    trusted_certs += int_certs
    verified = verify_chain_of_trust(cert, trusted_certs)
    if verified:
        print('Certificate verified')


def verify_chain_of_trust(cert_pem, trusted_cert_pems):
    certificate = crypto.load_certificate(crypto.FILETYPE_PEM, cert_pem)
    # Create and fill a X509Store with trusted certs
    store = crypto.X509Store()
    for trusted_cert_pem in trusted_cert_pems:
        trusted_cert = crypto.load_certificate(
            crypto.FILETYPE_PEM, trusted_cert_pem)
        store.add_cert(trusted_cert)

    # Create a X590StoreContext with the cert and trusted certs
    # and verify the the chain of trust
    store_ctx = crypto.X509StoreContext(store, certificate)
    # Returns None if certificate can be validated
    result = store_ctx.verify_certificate()
    if result is None:
        return True
    else:
        return False


print("Verfiying Twitter certificate...")
verify("twitter_com.cert", ["int_twitter_com.cert"], "ca-certificates.cert")

print("Verfiying Google certificate...")
verify("google_com.cert", ["int_google_com.cert",
       "int_google_com_2.cert"], "ca-certificates.cert")

print("Verfiying Chula certificate...")
verify("chula_ac_th.cert", ["int_chula_ac_th.cert"], "ca-certificates.cert")

print("Verfiying Classdeedee certificate...")
verify("classdeedee.cert", ["int_classdeedee.cert"], "ca-certificates.cert")
