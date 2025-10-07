from typing import Dict, Any
import sqlite3

from mcp.types import Resource

analytics_resource = Resource(
                    uri="mcp://gateway/analytics",
                    name="Usage Analytics",
                    description="Server usage statistics and metrics",
                    mimeType="application/json"
                )


async def get_analytics(db_path) -> Dict[str, Any]:
    """Get usage analytics"""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Get conversation stats
        cursor.execute("SELECT COUNT(*) FROM conversations")
        total_conversations = cursor.fetchone()[0]

        cursor.execute("SELECT model, COUNT(*) FROM conversations GROUP BY model")
        model_usage = dict(cursor.fetchall())

        cursor.execute("SELECT COUNT(*) FROM file_operations")
        total_file_ops = cursor.fetchone()[0]

        cursor.execute("SELECT operation, COUNT(*) FROM file_operations GROUP BY operation")
        operation_stats = dict(cursor.fetchall())

        conn.close()

        return {
            "total_conversations": total_conversations,
            "model_usage": model_usage,
            "total_file_operations": total_file_ops,
            "operation_stats": operation_stats,
            "uptime": "Available since server start"
        }
    except Exception as e:
        return {"error": str(e)}