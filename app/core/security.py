import bcrypt
import logging

async def verify_password(password:str,hashedPassword:str):
    logging.info("Verifying password with existing hashed password")
    try:
        encode_password = password.encode("utf-8")
        return bcrypt.checkpw(encode_password,hashedPassword.encode("utf-8"))
    except Exception as e:
        logging.error("error occured while verifying the password")
        raise e




