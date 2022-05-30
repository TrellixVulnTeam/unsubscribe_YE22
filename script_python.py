import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = 'inkeedin@gmail.com' #I
EMAIL_PASSWORD = 'Toto.123456'
contacts = ['chanahousna@gmail.com', 'houssnachana1999@gmail.com','jouffraultguillaume@gmail.com','miftaouhassane@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Ne pas répondre'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'chanahousna@gmail.com' #'luc.nicaud@depinfonancy.net'#'laurent.ciarletta@depinfonancy.net'#'houssnachana1999@gmail.com','jouffraultguillaume@gmail.com','miftaouhassane@gmail.com'
files=['LinkedIn_logo_initials.png']
msg.set_content('image attached ')
msg.add_alternative("""\
        <!DOCTYPE html>
    <html>
        <body>
            
            <br>
            <tr>
               
                <br/>
                 <tr>
                
                 <table role="presentation" style="width:100%!important;min-width:100%!important" width="100%" cellspacing="0" cellpadding="0" border="0"> 
                 <tbody> 
                 <tr> 
                 <td valign="middle" align="left">
                 <a href="https://www.linkedin.com/comm/feed/?midToken=AQGMlsIM_llh7Q&amp;midSig=1kQiO9BQt8-W01&amp;trk=eml-email_generic_invitation_reminder_organization_01-header-3-home&amp;trkEmail=eml-email_generic_invitation_reminder_organization_01-header-3-home-null-emxfn3%7Ekx8malg5%7Ed4-null-neptune%2Ffeed&amp;lipi=urn%3Ali%3Apage%3Aemail_email_generic_invitation_reminder_organization_01%3BckklbNYeRHC4qPRb0PQNeA%3D%3D" 
                 style="color:#0073b1;display:inline-block;text-decoration:none" target="_blank" > 
                 <img alt="LinkedIn" src="https://ci5.googleusercontent.com/proxy/HLJPoYaIjQCPmtZFUzA0GpWVjoqSw6RQ-MoR2Xr-rpowQlfvl-f9bZfODjdQVHq0hb8xmOVEoWxwDJbmiTs1f8DbxQoTwjQjLq0lOwLIaq6hCn0pP4gb782m2RNWGOijSOC7c0v1OANl8XeE-MCDNZr8AlK61gZpAGduKmnVPs016BiS5jRqEDr4kMb-A4WEAOx8sVEi9ihn7yyA-ACB2PI7Vs4OsFStAzC6Rm8mu9N96CQZOqLu-JI7_UueHUfb8bb_ACjPqfsSujMzDM1_I4c9qF0MzbDw6Hikf1gXPZbYCAtBSlZrLvBEwKoocg=s0-d-e1-ft#https://static.licdn.com/sc/p/com.linkedin.email-assets-frontend%3Aemail-assets-frontend-static-content%2B__latest__/f/%2Femail-assets-frontend%2Fimages%2Femail%2Fphoenix%2Flogos%2Flogo_phoenix_header_blue_78x66_v1.png" style="outline:none;color:#ffffff;text-decoration:none" class="CToWUd" width="40" height="34" border="0"></a></td> <td width="100%" valign="middle" align="right"><a href="https://www.linkedin.com/in/housna-chana/" style="margin:0;color:#0073b1;display:inline-block;text-decoration:none" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.linkedin.com/comm/in/guillaume-jouffrault-893492208?midToken%3DAQGMlsIM_llh7Q%26midSig%3D1kQiO9BQt8-W01%26trk%3Deml-email_generic_invitation_reminder_organization_01-header-11-profile%26trkEmail%3Deml-email_generic_invitation_reminder_organization_01-header-11-profile-null-emxfn3%257Ekx8malg5%257Ed4-null-neptune%252Fprofile%257Evanity%252Eview%26lipi%3Durn%253Ali%253Apage%253Aemail_email_generic_invitation_reminder_organization_01%253BckklbNYeRHC4qPRb0PQNeA%253D%253D&amp;source=gmail&amp;ust=1652777337637000&amp;usg=AOvVaw2mMdHiZYgrINGDSxEC8kJD"> <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0"> <tbody> <tr> <td style="padding:0 0 0 10px" valign="middle" align="left"><p style="margin:0;font-weight:400"> <span style="word-wrap:break-word;color:#4c4c4c;word-break:break-word;font-weight:400;font-size:14px;line-height:1.429"></span></p></td> <td style="padding-left:10px" width="40" valign="middle"> <img alt="" src="https://media-exp1.licdn.com/dms/image/C4E03AQH17K7dSmONmQ/profile-displayphoto-shrink_800_800/0/1652378544197?e=1659571200&v=beta&t=79slpawLXRL63-mfAlyrZ4eQSncbqc8wO_S56DkN2JQ" style="border-radius:50%;outline:none;color:#ffffff;text-decoration:none" class="CToWUd" jslog="138226; u014N:xr6bB; 53:W2ZhbHNlXQ.." width="36" height="36" border="0"></td> </tr> </tbody> </table></a></td> <td width="1">&nbsp;</td> </tr> </tbody> </table></tr>
                 <tbody> <tr> <td> <table role="presentation" style="font-family:Helvetica,Arial,sans-serif" 
                 width="100%" cellspacing="0" cellpadding="0" border="0"> 
                 <tbody> 
                 <tr> 
                 <td style="padding:16px 16px 24px 24px">
                  <table role="presentation" style="font-family:Helvetica,Arial,sans-serif" width="100%" cellspacing="0" 
                  cellpadding="0" border="0"> <tbody> <tr> <td style="padding-right:12px"> 
                  <img alt="" role="presentation" src="https://media-exp1.licdn.com/dms/image/C4E03AQH17K7dSmONmQ/profile-displayphoto-shrink_800_800/0/1652378544197?e=1658966400&v=beta&t=aN6zY4_uRJRYoUM8G3kjx08rwVsZ931U5I1klDjDsxE" 
                  style="border-radius:50%;outline:none;color:#ffffff;text-decoration:none" class="CToWUd" width="40" height="40" border="0">
                  </td> 
                  <td> 
                  <p style="margin:0;color:#4c4c4c;font-weight:400;font-size:16px;line-height:1.25">Chana Housna vous a invité(e) à vous abonner à une page la semaine dernière</p></td> </tr> </tbody> 
                  </table>
                  </td> 
                  </tr> 
                  <tr> 
                  <td style="padding:0 24px 24px 24px"> <table role="presentation" 
                  style="font-family:Helvetica,Arial,sans-serif" width="100%" cellspacing="0" cellpadding="0" border="0"> 
                  <tbody> <tr> <td style="display:inline-block;width:60px;padding-right:12px" width="60"> 
                  <table role="presentation" style="font-family:Helvetica,Arial,sans-serif" width="100%" cellspacing="0" 
                  cellpadding="0" border="0"> <tbody> <tr> <td> 
      
                  </td> </tr> </tbody> </table></td> 
                  <td style="display:inline-block;width:initial;vertical-align:top" valign="top"> 
                  <table role="presentation" style="font-family:Helvetica,Arial,sans-serif" width="100%" 
                  cellspacing="0" cellpadding="0" border="0"> <tbody> <tr> <td><span style="display:inline;
                  padding-bottom:4px"> <h2 style="margin:0;word-wrap:break-word;color:#262626;word-break:break-word;
                  font-weight:700;font-size:16px;line-height:1.5">Finance Club </h2>
                  </span>
                  </td> 
                  </tr> 
                  <tr> <td style="padding-bottom:8px"> 
                  <p style="margin:0;color:#4c4c4c;font-weight:400;font-size:14px;line-height:1.429">Information Services</p>
                  </td> 
                  </tr> 
                  <tr> 
                  <td>
                  <span style="padding:0 6px 6px 0;display:inline-block"> 
                  <table style="display:inline-block" cellspacing="0" cellpadding="0" border="0"> <tbody> 
                  <tr> <td valign="middle" align="center">
                  <a href="https://iridescent-croquembouche-4b8508.netlify.app/" style="word-wrap:normal;color:#0073b1;
                  word-break:normal;white-space:nowrap;display:block;text-decoration:none" target="_blank" 
                  data-saferedirecturl=""> 
                  <table role="presentation" width="auto" cellspacing="0" cellpadding="0" border="0"> 
                  <tbody> 
                  <tr> 
                  <td style="padding:6px 16px;color:#ffffff;font-weight:500;font-size:16px;border-color:#0073b1;background-color:#0073b1;border-radius:2px;border-width:1px;border-style:solid" bgcolor="#0073B1">
                  <a href="https://www.linkedin.com/comm/company/80415400/accept-follow-invite/6875896597998248022/FmBErK0v?midToken=AQGMlsIM_llh7Q&midSig=1kQiO9BQt8-W01&trk=eml-email_generic_invitation_reminder_organization_01-pending_invites-2-generic&trkEmail=eml-email_generic_invitation_reminder_organization_01-pending_invites-2-generic-null-emxfn3%7Ekx8malg5%7Ed4-null-voyagerOffline&lipi=urn%3Ali%3Apage%3Aemail_email_generic_invitation_reminder_organization_01%3BckklbNYeRHC4qPRb0PQNeA%3D%3D" style="color:#ffffff;display:inline-block;text-decoration:none" target="_blank" 
                  data-saferedirecturl="">
                 Accept
                 </a>
                 </td> 
                 </tr> 
                 </tbody> 
                 </table>
                 </a>
                 </td> 
                 </tr> 
                 </tbody> 
                 </table>
                  <table style="display:inline-block" cellspacing="0" cellpadding="0" border="0"> 
                  <tbody> <tr> <td valign="middle" align="center">
                 <a href="https://iridescent-croquembouche-4b8508.netlify.app/" style="word-wrap:normal;color:#0073b1;word-break:normal;white-space:nowrap;display:block;text-decoration:none" target="_blank" 
                 > <table role="presentation" width="auto" cellspacing="0" cellpadding="0" border="0"> <tbody> <tr> <td style="border-radius:2px;padding:6px 16px;color:#4c4c4c;font-weight:500;font-size:16px;border-color:#737373;border-width:1px;border-style:solid">
                 <a href="https://www.linkedin.com/comm/company/80415400/accept-follow-invite/6875896597998248022/FmBErK0v?midToken=AQGMlsIM_llh7Q&midSig=1kQiO9BQt8-W01&trk=eml-email_generic_invitation_reminder_organization_01-pending_invites-2-generic&trkEmail=eml-email_generic_invitation_reminder_organization_01-pending_invites-2-generic-null-emxfn3%7Ekx8malg5%7Ed4-null-voyagerOffline&lipi=urn%3Ali%3Apage%3Aemail_email_generic_invitation_reminder_organization_01%3BckklbNYeRHC4qPRb0PQNeA%3D%3D" style="color:#4c4c4c;display:inline-block;text-decoration:none" target="_blank" 
                 >View page</a></td> </tr> </tbody> </table></a></td> </tr> </tbody> </table></span></td> </tr> </tbody> </table></td> </tr> </tbody> </table></td> </tr> </tbody> </table></td> </tr> </tbody> 
                  <td> 
                    <table role="presentation" style="background-color:#edf0f3;padding:0 24px;color:#6a6c6d;text-align:center" width="100%" cellspacing="0" cellpadding="0" border="0" bgcolor="#EDF0F3" align="center"> 
                        <tbody> 
                            <tr> 
                                <td style="padding:16px 0 0 0;text-align:center" align="center"> 
                                    <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" align="center"> <tbody> <tr> <td style="padding:0 0 16px 0;vertical-align:middle;text-align:center" valign="middle" align="center">
                                    <a href="https://iridescent-croquembouche-4b8508.netlify.app/?user=chanahousna@gmail.com" style="color:#6a6c6d;text-decoration:underline;display:inline-block" target="_blank" 
                                    data-saferedirecturl="https://iridescent-croquembouche-4b8508.netlify.app/"> 
                                    <span style="color:#6a6c6d;font-weight:400;text-decoration:underline;font-size:12px;line-height:1.333">Se désinscrire</span></a>&nbsp;&nbsp;|&nbsp;&nbsp;
                                    <a href="https://www.linkedin.com/e/v2?e=emxfn3-kx8malg5-d4&lipi=urn%3Ali%3Apage%3Aemail_email_generic_invitation_reminder_organization_01%3BckklbNYeRHC4qPRb0PQNeA%3D%3D&a=customerServiceUrl&midToken=AQGMlsIM_llh7Q&midSig=1kQiO9BQt8-W01&ek=email_generic_invitation_reminder_organization_01&li=7&m=footer&ts=help&articleId=67" style="color:#6a6c6d;text-decoration:underline;display:inline-block" target="_blank" 
                                    data-saferedirecturl="https://iridescent-croquembouche-4b8508.netlify.app/"> 
                                    <span style="color:#6a6c6d;font-weight:400;text-decoration:underline;font-size:12px;line-height:1.333">Aide
                                    </span>
                                    </a>
                                    </td> 
                                    </tr> 
                                    </tbody> 
                                    </table>
                                    </td> 
                                    </tr> 
                                    <tr> 
                                        <td> 
                                            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0"> 
                                            <tbody> 
                                            <tr> 
                                            <td style="padding:0 0 12px 0;text-align:center" align="center"> 
                                            <p style="margin:0;color:#6a6c6d;font-weight:400;font-size:12px;line-height:1.333">
                                            Vous recevez des e-mails concernant Pages Invitation.</p>
                                            </td> 
                                            </tr> 
                                            <tr> 
                                            <td style="padding:0 0 12px 0;text-align:center" align="center"> 
                                            <p style="margin:0;word-wrap:break-word;color:#6a6c6d;word-break:break-word;font-weight:400;font-size:12px;line-height:1.333">
                                            
                                            <a href="https://www.linkedin.com/e/v2?e=emxfn3-kx8malg5-d4&amp;lipi=urn%3Ali%3Apage%3Aemail_email_generic_invitation_reminder_organization_01%3BckklbNYeRHC4qPRb0PQNeA%3D%3D&amp;a=customerServiceUrl&amp;midToken=AQGMlsIM_llh7Q&amp;midSig=1kQiO9BQt8-W01&amp;ek=email_generic_invitation_reminder_organization_01&amp;articleId=4788" 
                                            style="color:#6a6c6d;text-decoration:underline;display:inline-block" target="_blank" 
                                            data-saferedirecturl="https://www.google.com/url?q=https://www.linkedin.com/e/v2?e%3Demxfn3-kx8malg5-d4%26lipi%3Durn%253Ali%253Apage%253Aemail_email_generic_invitation_reminder_organization_01%253BckklbNYeRHC4qPRb0PQNeA%253D%253D%26a%3DcustomerServiceUrl%26midToken%3DAQGMlsIM_llh7Q%26midSig%3D1kQiO9BQt8-W01%26ek%3Demail_generic_invitation_reminder_organization_01%26articleId%3D4788&amp;source=gmail&amp;ust=1652777337638000&amp;usg=AOvVaw2anOOhlhVVnMObog75S6j1">
                                            Découvrez pourquoi nous précisons ceci.</a>
                                            </p>
                                            </td> 
                                            </tr> 
                                            <tr> 
                                            <td style="padding:0 0 8px 0;text-align:center" align="center">
                                            <a href="https://www.linkedin.com/comm/feed/?midToken=AQGMlsIM_llh7Q&amp;midSig=1kQiO9BQt8-W01&amp;trk=eml-email_generic_invitation_reminder_organization_01-footer-5-home&amp;trkEmail=eml-email_generic_invitation_reminder_organization_01-footer-5-home-null-emxfn3%7Ekx8malg5%7Ed4-null-neptune%2Ffeed&amp;lipi=urn%3Ali%3Apage%3Aemail_email_generic_invitation_reminder_organization_01%3BckklbNYeRHC4qPRb0PQNeA%3D%3D" style="color:#6a6c6d;text-decoration:underline;display:inline-block" target="_blank" 
                                            data-saferedirecturl="https://www.google.com/url?q=https://www.linkedin.com/comm/feed/?midToken%3DAQGMlsIM_llh7Q%26midSig%3D1kQiO9BQt8-W01%26trk%3Deml-email_generic_invitation_reminder_organization_01-footer-5-home%26trkEmail%3Deml-email_generic_invitation_reminder_organization_01-footer-5-home-null-emxfn3%257Ekx8malg5%257Ed4-null-neptune%252Ffeed%26lipi%3Durn%253Ali%253Apage%253Aemail_email_generic_invitation_reminder_organization_01%253BckklbNYeRHC4qPRb0PQNeA%253D%253D&amp;source=gmail&amp;ust=1652777337638000&amp;usg=AOvVaw3DcOj6SshbzjYjIYay6QUv">
                                            <img alt="LinkedIn" src="https://ci3.googleusercontent.com/proxy/bzvgSwnIl-EoSvCPlRKIZXuV6yP_TY2wfudBIPShxs0xlsLFtMTHIe6DzN4h8xe9DYK9VB_3WFvW1yMlgrDINNtVDKklKGGN6A4_XMx5wgyGRD_hJf5P7COhOv2ob-4L3n9pnocTO2GxJCqn1GBUAYenkreWS21wfATmwZ1eaQ8X6nsSos8jt0nyinhwkCDEN1mbUUEK4FWsOGPKF0zGoAUKEIMnYGmtmACPsMz2fn1JtNBlOnDdW544dBqa-677tO8KrDJ1XHmClWb2sN7anUokaeZPJ53XVILvNZa0VczDPOMTCY-tPyNtLEAjdc48A8_9=s0-d-e1-ft#https://static.licdn.com/sc/p/com.linkedin.email-assets-frontend%3Aemail-assets-frontend-static-content%2B__latest__/f/%2Femail-assets-frontend%2Fimages%2Femail%2Fphoenix%2Flogos%2Flogo_phoenix_footer_darkgray_197x48_v1.png" style="outline:none;color:#ffffff;display:block;text-decoration:none"
                                             class="CToWUd" width="58" height="14" border="0"></a></td> </tr> <tr> <td style="padding:0 0 12px 0;text-align:center" align="center"> <p style="margin:0;color:#6a6c6d;font-weight:400;font-size:12px;line-height:1.333">© 2021 LinkedIn Ireland Unlimited Company, Wilton Plaza, Wilton Place, Dublin 2. LinkedIn est le nom commercial déposé de LinkedIn Ireland Unlimited Company. LinkedIn et le logo de LinkedIn sont des marques déposées de LinkedIn.</p>
                                                 </td> 
                                                 </tr> 
                                                 </tbody> 
                                                 </table>
                                                 </td> 
                                                 </tr> 
                                                 </tbody> 
                                                 </table>
                  </td> 

               

        </body>
    </html>
    """, subtype='html')


# for file in files :
#     with open(file,'rb') as f:
#         file_data=f.read()
#         file_type=imghdr.what(f.name)
#         file_name=f.name
#     msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)



with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    try :
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print('done')
    
    except smtplib.SMTPResponseException as e:
        error_code = e.smtp_code
        error_message = e.smtp_error
