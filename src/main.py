import fire
import cli

if __name__ == "__main__":
    fire.Fire({
        "price": cli.price,
        "baseinfo": cli.companyInfo,
        "compinfo": cli.marketInfo
    })





