type OutreachReportRow = {
  status: string;
  eventId?: string;
};

export function countSentRows(report: OutreachReportRow[]): number {
  return report.filter((row) => row.status === "sent" && Boolean(row.eventId)).length;
}
