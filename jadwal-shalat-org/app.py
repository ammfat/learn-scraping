from ScrapPS.scrap_ps import ScrapPS

def main():
    url = 'https://jadwalsholat.org/adzan/monthly.php?id=94'
    scrap_ps = ScrapPS(url)

    pray_schedule = scrap_ps.get_pray_time()

    print("\n-- MOSLEM PRAY SCHEDULE --\n")
    print(f"Source\t: {scrap_ps.get_url()} [{scrap_ps.get_response().status_code}]")
    print(f"Region\t: Indonesia, {scrap_ps.get_region_timezone()[0]} ({scrap_ps.get_region_timezone()[1]})")
    print(f"Date\t: {pray_schedule['Imsyak'].date()}\n")

    for key, value in pray_schedule.items():
        print(f"{key}\t: {value.time()}")

if __name__ == "__main__":
    main()
