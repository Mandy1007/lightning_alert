import click, json, sys, quadkey

@click.command()
@click.argument('assets_file')
def cli(assets_file):
    """Given a lighting alert for a specific area"""
    with open(assets_file) as f:
        assets_data = json.load(f)
    assets_dict = {}  # save the data as a dict format to improve execution efficiency
    count_aline = 0
    for asset in assets_data:
        count_aline += 1
        try:
            if asset["quadKey"] not in assets_dict:
                assets_dict[asset["quadKey"]] = [(asset["assetOwner"], asset["assetName"])]
            else:
                assets_dict[asset["quadKey"]].append((asset["assetOwner"], asset["assetName"]))
        except Exception as e:
            click.echo(click.style("Invalid asset input #%s: "+str(asset) % count_aline,fg = 'red'))
    """Since quadkey might not be accurate enough
    there might be more than one asset owners sharing a same quadkey
    """
    count_lline = 0
    for line in sys.stdin:
        lightning_data = json.loads(line)
        count_lline += 1
        try:
            if lightning_data["flashType"] == 9: # exclude flashType is 'heartbeat'
                continue
            latitude = lightning_data['latitude']
            longitude = lightning_data['longitude']
            qk = quadkey.from_geo((latitude, longitude), 12) # conver lightning data to quadkey
            if qk.key in assets_dict:
                asset_tuples = assets_dict[qk.key]
                for asset in asset_tuples:
                    click.echo('lightning alert for %s : %s' % (asset[0], asset[1]))
                del assets_dict[qk.key] # to prevent alerting several times
        except Exception as e:
            click.echo(click.style("Invalid strike input #%s: "+str(line) % count_lline, fg = 'red'))
