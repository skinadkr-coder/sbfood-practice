from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    agencies = [
        ("서울대리점", "A", 500000),
        ("부산대리점", "B", 300000),
        ("대구대리점", "A", 200000),
        ("인천대리점", "B", 150000),
        ("광주대리점", "A", 100000),
    ]

    rows = ""
    for name, grade, order_amount in agencies:
        if grade == "A":
            fee_rate = 0.05
        elif grade == "B":
            fee_rate = 0.10
        else:
            fee_rate = 0

        fee = int(order_amount * fee_rate)
        rows += f"""
        <tr>
            <td>{name}</td>
            <td>{grade}등급</td>
            <td>{order_amount:,}원</td>
            <td>{fee:,}원</td>
        </tr>
        """

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>승빈푸드 정산 관리</title>
        <style>
            body {{ font-family: 맑은 고딕; padding: 40px; background: #f5f5f5; }}
            h1 {{ color: #333; }}
            table {{ border-collapse: collapse; width: 600px; background: white; }}
            th {{ background: #4CAF50; color: white; padding: 12px; }}
            td {{ padding: 10px; border-bottom: 1px solid #ddd; text-align: center; }}
            tr:hover {{ background: #f0f0f0; }}
        </style>
    </head>
    <body>
        <h1>승빈푸드 대리점별 수수료 정산</h1>
        <table>
            <tr>
                <th>대리점명</th>
                <th>등급</th>
                <th>주문금액</th>
                <th>수수료</th>
            </tr>
            {rows}
        </table>
    </body>
    </html>
    """
    return html

app.run(debug=True)
