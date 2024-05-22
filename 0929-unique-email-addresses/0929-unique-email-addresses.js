/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
    let uniqueEmails = new Set();
    emails.forEach(email => {
        let parts = email.split('@');
        let local = parts[0];
        let domain = parts[1];
        local = local.split('+')[0];
        local = local.replace(/\./g, '');
        email = local + "@" + domain;
        uniqueEmails.add(email);
    });
    return uniqueEmails.size;
};